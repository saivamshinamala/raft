"""
pdf_to_jsonl.py

Simple, offline-friendly script to extract structured, page-by-page JSONL from complex PDFs
(using pdfplumber for layout + tables and a local Llama3-8B-Instruct model to semantically
structure the extracted content into a RAFT-friendly JSON schema).

Requirements (install locally):
    pip install pdfplumber transformers torch sentencepiece

If the PDF pages are scanned images, enable OCR by installing:
    pip install pytesseract pdf2image
and have Tesseract and poppler installed on your machine.

Usage:
    python pdf_to_jsonl.py --pdf input.pdf --out output.jsonl --model_path /path/to/llama3-8b-instruct \
        --device cuda

Notes:
- Set model_path to the local directory containing your Llama3-8B-Instruct-compatible model files.
- The script processes the PDF page-by-page and asks the local Llama model to convert the
  extracted raw elements (headings, paragraphs, tables) into a clean JSON object per page.
- Output is JSONL: one JSON object per line, suitable for RAFT / RAG fine-tuning.
"""

import argparse
import json
import math
from pathlib import Path
from typing import List, Dict, Any

import pdfplumber
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# -----------------------------
# Helpers: PDF extraction
# -----------------------------


def group_chars_to_lines(chars: List[Dict[str, Any]], y_tolerance: float = 3.0) -> List[Dict]:
    """
    Group pdfplumber page.chars into text lines based on 'top' coordinate proximity.
    Returns list of dict {text, top, size_mean, words}
    """
    if not chars:
        return []
    # sort by top then x0
    chars = sorted(chars, key=lambda c: (round(c["top"]), c.get("x0", 0)))
    lines = []
    current_line = {"top": chars[0]["top"], "chars": [chars[0]]}
    for ch in chars[1:]:
        if abs(ch["top"] - current_line["top"]) <= y_tolerance:
            current_line["chars"].append(ch)
        else:
            # flush
            text = "".join(c["text"] for c in current_line["chars"])
            sizes = [c.get("size", 0) for c in current_line["chars"]]
            lines.append({"text": text.strip(), "top": current_line["top"], "size_mean": float(sum(sizes) / len(sizes)), "raw_chars": current_line["chars"]})
            current_line = {"top": ch["top"], "chars": [ch]}
    # last
    text = "".join(c["text"] for c in current_line["chars"])
    sizes = [c.get("size", 0) for c in current_line["chars"]]
    lines.append({"text": text.strip(), "top": current_line["top"], "size_mean": float(sum(sizes) / len(sizes)), "raw_chars": current_line["chars"]})
    return lines


def detect_headings(lines: List[Dict], multiplier: float = 1.15) -> List[str]:
    """
    Simple heuristic: treat lines with mean font size greater than multiplier * median_size as headings.
    Returns list of heading strings (in reading order).
    """
    if not lines:
        return []
    sizes = [l["size_mean"] for l in lines if l["size_mean"] > 0]
    if not sizes:
        return []
    median_size = sorted(sizes)[len(sizes) // 2]
    threshold = median_size * multiplier
    headings = [l["text"] for l in lines if l["size_mean"] >= threshold and len(l["text"].strip()) > 2]
    return headings


def extract_tables_from_page(page) -> List[Dict[str, Any]]:
    """
    Use pdfplumber's table extraction. Convert to a JSON-friendly structure.
    Each table: {rows: [[cell,...], ...], header: [col1, ...] or None, structured_rows: [ {col:val}, ... ] }
    """
    tables = []
    try:
        raw_tables = page.extract_tables() or []
    except Exception:
        raw_tables = []
    for t in raw_tables:
        # normalize rows: ensure all cells are strings (strip)
        rows = [[(cell.strip() if cell is not None else "") for cell in row] for row in t]
        header = None
        structured_rows = []
        if rows:
            # heuristics: if first row contains non-empty distinct values => header
            first = rows[0]
            non_empty = sum(1 for c in first if c)
            if non_empty >= 1 and any(not any(c.strip().isdigit() for c in cell) for cell in first):
                header = first
                for r in rows[1:]:
                    # map header->cell
                    obj = {header[i] if i < len(header) and header[i] else f"col_{i+1}": (r[i] if i < len(r) else "") for i in range(max(len(header), len(r)))}
                    structured_rows.append(obj)
            else:
                # no header detected, create generic columns
                maxcols = max(len(r) for r in rows)
                header = [f"col_{i+1}" for i in range(maxcols)]
                for r in rows:
                    obj = {header[i]: (r[i] if i < len(r) else "") for i in range(maxcols)}
                    structured_rows.append(obj)
        tables.append({"rows": rows, "header": header, "structured_rows": structured_rows})
    return tables


def extract_page_elements(page) -> Dict[str, Any]:
    """
    Extract headings, paragraphs (as blocks), and tables from a pdfplumber page.
    Paragraphs are built by grouping text by tolerance of vertical spacing.
    """
    # Extract chars to build lines and detect headings
    chars = page.chars  # list of dicts
    lines = group_chars_to_lines(chars)
    headings = detect_headings(lines)

    # Build paragraph blocks using pdfplumber.extract_text or merging lines with small vertical gaps
    raw_text = page.extract_text(x_tolerance=2) or ""
    # naive paragraph split: split by double newline or large gaps between lines
    paragraphs = [p.strip() for p in raw_text.split("\n\n") if p.strip()]
    if not paragraphs:
        # fallback: join groups of lines into paragraphs by proximity
        paragraphs = []
        if lines:
            cur = lines[0]["text"]
            prev_top = lines[0]["top"]
            for l in lines[1:]:
                if abs(l["top"] - prev_top) > 12:  # big gap -> new paragraph
                    paragraphs.append(cur.strip())
                    cur = l["text"]
                else:
                    cur += " " + l["text"]
                prev_top = l["top"]
            paragraphs.append(cur.strip())

    tables = extract_tables_from_page(page)

    return {"headings": headings, "paragraphs": paragraphs, "tables": tables}


# -----------------------------
# Helpers: Llama-based structuring
# -----------------------------


PROMPT_TEMPLATE = """
You are a helpful assistant that converts raw PDF page extraction data into a single, clean JSON object.
The JSON MUST follow this schema exactly (no extra top-level keys):

{{
  "page_number": <int>,
  "headings": [ <list of heading strings in reading order> ],
  "paragraphs": [ <list of paragraph strings in reading order> ],
  "tables": [
    {{
      "header": [<header column names>] or null,
      "rows": [ [cell1, cell2, ...], ... ],
      "structured_rows": [ {{col1: val, col2: val, ...}}, ... ],
      "notes": "<short note about the table, e.g., 'detected header' or 'no header'>"
    }},
    ...
  ],
  "summary": "<a concise 1-2 sentence summary of the page content>",
  "important_entities": [ "<short list of important entities, e.g. section names, numbers, dates>" ]
}}

Now convert the following extracted raw data into the JSON schema above.
Only output valid JSON. If something is empty, use empty list [] or null for header.

Raw data:
{raw}

Remember:
- Keep 'summary' to at most two sentences.
- 'important_entities' should be up to ~8 short tokens identifying things a retriever might want to index.
- Output only JSON (no preamble).
"""

def load_model_and_tokenizer(model_path: str, device: str = "cpu"):
    """
    Load a local Llama-family model and tokenizer. Adjust for your local setup.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16 if device.startswith("cuda") else torch.float32, trust_remote_code=True)
    if device.startswith("cuda"):
        model = model.to(device)
    return tokenizer, model


def generate_structured_json(tokenizer, model, prompt: str, device: str = "cpu", max_new_tokens: int = 512, temperature: float = 0.0) -> str:
    """
    Generate text from model. Returns the raw string output.
    """
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=4096 - max_new_tokens)
    input_ids = inputs["input_ids"]
    if device.startswith("cuda"):
        input_ids = input_ids.cuda()
        model = model.to("cuda")
    with torch.no_grad():
        out_ids = model.generate(input_ids=input_ids, max_new_tokens=max_new_tokens, temperature=temperature, do_sample=False, eos_token_id=tokenizer.eos_token_id)
    output = tokenizer.decode(out_ids[0][input_ids.shape[-1]:], skip_special_tokens=True)
    # Combine any initial artifacts (some models may print newline); try to extract JSON substring
    text = output.strip()
    # Try to find the first '{' and last '}' to parse JSON
    if "{" in text and "}" in text:
        start = text.find("{")
        end = text.rfind("}") + 1
        text = text[start:end]
    return text


# -----------------------------
# Main driver
# -----------------------------


def process_pdf_to_jsonl(pdf_path: str, out_path: str, model_path: str, device: str = "cpu", ocr: bool = False):
    pdf_path = Path(pdf_path)
    out_path = Path(out_path)
    tokenizer, model = load_model_and_tokenizer(model_path, device=device)

    results = []
    with pdfplumber.open(pdf_path) as pdf, open(out_path, "w", encoding="utf-8") as fout:
        for i, page in enumerate(pdf.pages, start=1):
            page_elems = extract_page_elements(page)
            # Build raw input for the model, keeping it concise:
            raw_for_model = {
                "page_number": i,
                "headings": page_elems["headings"],
                "paragraphs_sample": page_elems["paragraphs"][:10],  # limit to first 10 paras to keep prompt small
                "tables": [{"rows": t["rows"], "header": t["header"]} for t in page_elems["tables"]],
            }
            prompt = PROMPT_TEMPLATE.format(raw=json.dumps(raw_for_model, ensure_ascii=False, indent=2))
            print(f"Processing page {i} ...")
            generated = generate_structured_json(tokenizer, model, prompt, device=device)

            try:
                parsed = json.loads(generated)
            except Exception as e:
                # If the model output isn't strict JSON, attempt to salvage by searching for JSON substring
                try:
                    start = generated.find("{")
                    end = generated.rfind("}") + 1
                    parsed = json.loads(generated[start:end])
                except Exception as e2:
                    # fallback: use basic structured content without model help
                    print(f"Warning: failed to parse model output on page {i}: {e}; using fallback structure.")
                    parsed = {
                        "page_number": i,
                        "headings": page_elems["headings"],
                        "paragraphs": page_elems["paragraphs"],
                        "tables": page_elems["tables"],
                        "summary": "",
                        "important_entities": [],
                    }
            # Ensure page_number present
            parsed.setdefault("page_number", i)
            # Write as single-line JSON (jsonl)
            fout.write(json.dumps(parsed, ensure_ascii=False) + "\n")
            fout.flush()
    print(f"Saved JSONL to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract PDF and convert pages to RAFT-friendly JSONL using a local Llama model.")
    parser.add_argument("--pdf", required=True, help="Input PDF file path")
    parser.add_argument("--out", required=True, help="Output JSONL file path")
    parser.add_argument("--model_path", required=True, help="Local path to Llama3-8B-Instruct-compatible model")
    parser.add_argument("--device", default="cpu", choices=["cpu", "cuda"], help="Device to run model on")
    parser.add_argument("--ocr", action="store_true", help="Enable OCR fallback for scanned PDFs (requires pytesseract and pdf2image)")
    args = parser.parse_args()
    process_pdf_to_jsonl(args.pdf, args.out, args.model_path, device=args.device, ocr=args.ocr)
