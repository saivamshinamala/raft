"""
pdf_to_jsonl_fast.py

Faster, GPU-optimized PDF -> RAFT-friendly JSONL extractor using a local Llama (Llama3-8B-Instruct).
Key speedups compared to a naive per-page LLM call:
 - Do deterministic extraction (pdfplumber) for all pages quickly.
 - Create a compact "raw" object per page (truncate long fields).
 - Batch multiple pages into a single LLM prompt so the model processes many pages per generate() call.
 - Use GPU (cuda) and fp16 to accelerate generation.
 - Use small deterministic generation settings (temperature=0, do_sample=False).
 - Write enriched JSONL output (per page) with additional metadata useful for RAFT/RAG.

Usage:
    python pdf_to_jsonl_fast.py --pdf "data/pdf/Shakti Userhand Book for Bot.pdf" --out data/pdf_chunks/output_chunks_enriched.jsonl --model_path E:/Meta-Llama-3-8B-Instruct --batch_size 6 --device cuda

Notes:
 - This script expects a local HF-style model directory compatible with transformers (trust_remote_code=True).
 - If you have a different runtime (llama.cpp / ggml), you can still use the deterministic extraction
   portion and feed the batch prompts to your inference runtime; adapt generate() calls accordingly.
 - For very large PDFs, tune batch_size and max_new_tokens. Start with batch_size=4..8.
"""

import argparse
import json
import math
import time
from pathlib import Path
from typing import List, Dict, Any

import pdfplumber
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# -----------------------------
# Heuristic extraction helpers
# -----------------------------


def group_chars_to_lines(chars: List[Dict[str, Any]], y_tolerance: float = 3.0) -> List[Dict]:
    if not chars:
        return []
    chars = sorted(chars, key=lambda c: (round(c.get("top", 0)), c.get("x0", 0)))
    lines = []
    cur_top = chars[0]["top"]
    cur_chars = [chars[0]]
    for ch in chars[1:]:
        if abs(ch["top"] - cur_top) <= y_tolerance:
            cur_chars.append(ch)
        else:
            text = "".join(c.get("text", "") for c in cur_chars).strip()
            sizes = [c.get("size", 0) for c in cur_chars if "size" in c]
            size_mean = float(sum(sizes) / len(sizes)) if sizes else 0.0
            lines.append({"text": text, "top": cur_top, "size_mean": size_mean})
            cur_top = ch["top"]
            cur_chars = [ch]
    if cur_chars:
        text = "".join(c.get("text", "") for c in cur_chars).strip()
        sizes = [c.get("size", 0) for c in cur_chars if "size" in c]
        size_mean = float(sum(sizes) / len(sizes)) if sizes else 0.0
        lines.append({"text": text, "top": cur_top, "size_mean": size_mean})
    return lines


def detect_headings(lines: List[Dict], multiplier: float = 1.15) -> List[str]:
    sizes = [l["size_mean"] for l in lines if l.get("size_mean", 0) > 0]
    if not sizes:
        return []
    median = sorted(sizes)[len(sizes) // 2]
    thresh = median * multiplier
    return [l["text"] for l in lines if l.get("size_mean", 0) >= thresh and len(l.get("text", "")) > 2]


def extract_tables_from_page(page) -> List[Dict[str, Any]]:
    tables = []
    try:
        raw_tables = page.extract_tables() or []
    except Exception:
        raw_tables = []
    for t in raw_tables:
        rows = [[(cell.strip() if cell is not None else "") for cell in row] for row in t]
        header = None
        structured_rows = []
        if rows:
            first = rows[0]
            non_empty = sum(1 for c in first if c)
            if non_empty >= 1 and any(not all(ch.isdigit() for ch in (cell or "")) for cell in first):
                header = first
                for r in rows[1:]:
                    obj = {header[i] if i < len(header) and header[i] else f"col_{i+1}": (r[i] if i < len(r) else "") for i in range(max(len(header), len(r)))}
                    structured_rows.append(obj)
            else:
                maxcols = max(len(r) for r in rows)
                header = [f"col_{i+1}" for i in range(maxcols)]
                for r in rows:
                    obj = {header[i]: (r[i] if i < len(r) else "") for i in range(maxcols)}
                    structured_rows.append(obj)
        tables.append({"rows": rows, "header": header, "structured_rows": structured_rows})
    return tables


def extract_page_elements_simple(page) -> Dict[str, Any]:
    # fast layout heuristics
    chars = getattr(page, "chars", []) or []
    lines = group_chars_to_lines(chars)
    headings = detect_headings(lines)

    # Use pdfplumber text extraction (fast)
    raw_text = page.extract_text(x_tolerance=2) or ""
    # split into paragraphs (simple)
    paragraphs = [p.strip() for p in raw_text.split("\n\n") if p.strip()]
    if not paragraphs and lines:
        # fallback: group lines by vertical gaps
        paragraphs = []
        cur = lines[0]["text"]
        prev_top = lines[0]["top"]
        for l in lines[1:]:
            if abs(l["top"] - prev_top) > 12:
                paragraphs.append(cur.strip())
                cur = l["text"]
            else:
                cur += " " + l["text"]
            prev_top = l["top"]
        paragraphs.append(cur.strip())

    tables = extract_tables_from_page(page)
    return {"headings": headings, "paragraphs": paragraphs, "tables": tables, "raw_text": raw_text}


# -----------------------------
# LLM prompt + batch handling
# -----------------------------


BATCH_PROMPT_TEMPLATE = """
You are a strict JSON generator. Convert the provided list of raw PDF page extraction objects into
a JSON array of page objects following this exact schema for each page:

{{
  "page_number": <int>,
  "chunk_id": "<string>",              // unique id like file_page_{n}
  "source_file": "<string>",           // input filename
  "page_numbers": [<int>],
  "headings": [<strings>],
  "paragraphs": [<strings>],
  "tables": [
    {{
      "header": [<strings>] or null,
      "rows": [ [cell1, cell2, ...], ... ],
      "structured_rows": [ {{col: val, ...}}, ... ],
      "notes": "<short note>"
    }}
  ],
  "document_text": "<concise concatenation used for retrieval>",
  "summary": "<1-2 sentence summary>",
  "important_entities": [ "<short list of up to 8 tokens>" ],
  "meta": {{ "ocr": false, "confidence": null }}
}}

Only output valid JSON: an array of page objects. If a field is missing, use [] or null as appropriate.
Keep 'summary' concise (max 2 sentences) and 'important_entities' short tokens.
Do not include any extra commentary or text outside the JSON array.

Raw pages:
{raw}
"""

def build_raw_for_model(page_elems: Dict[str, Any], page_number: int, source_file: str,
                        paras_limit: int = 6, table_row_limit: int = 6) -> Dict[str, Any]:
    # Truncate paragraphs and tables for prompt brevity while keeping enough context.
    paragraphs = page_elems.get("paragraphs", [])[:paras_limit]
    tables_sample = []
    for t in page_elems.get("tables", [])[:6]:
        rows = t.get("rows", [])[:table_row_limit]
        header = t.get("header")
        structured = t.get("structured_rows", [])[:table_row_limit]
        tables_sample.append({"header": header, "rows": rows, "structured_rows": structured})
    return {
        "page_number": page_number,
        "headings": page_elems.get("headings", []),
        "paragraphs": paragraphs,
        "tables": tables_sample,
        # small excerpt used for potential deterministic fallback
        "text_excerpt": (page_elems.get("raw_text") or "")[:4000],
        "source_file": source_file,
    }


def generate_batch_json(tokenizer, model, batch_raw: List[Dict[str, Any]], source_file: str, device: str,
                        max_new_tokens: int = 320, temperature: float = 0.0) -> str:
    """
    Build prompt for a list of page raw objects and generate JSON array output.
    """
    # compact JSON string for raw pages to reduce prompt size
    raw = json.dumps(batch_raw, ensure_ascii=False, separators=(",", ":"), indent=2)
    prompt = BATCH_PROMPT_TEMPLATE.format(raw=raw)

    # Tokenize once and generate on GPU
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=4096 - max_new_tokens)
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)

    with torch.no_grad():
        out_ids = model.generate(input_ids=input_ids,
                                 attention_mask=attention_mask,
                                 max_new_tokens=max_new_tokens,
                                 temperature=temperature,
                                 do_sample=False,
                                 eos_token_id=tokenizer.eos_token_id,
                                 pad_token_id=tokenizer.pad_token_id)
    # decode only generated tokens (skip input part)
    gen = tokenizer.decode(out_ids[0][input_ids.shape[-1]:], skip_special_tokens=True)
    text = gen.strip()
    # try to extract JSON array substring
    if "[" in text and "]" in text:
        start = text.find("[")
        end = text.rfind("]") + 1
        return text[start:end]
    else:
        return text  # fallback - may be non-JSON; caller will handle


# -----------------------------
# Main pipeline
# -----------------------------


def load_model_and_tokenizer(model_path: str, device: str = "cuda"):
    # Use fp16 for GPU
    dtype = torch.float16 if device.startswith("cuda") else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=dtype, trust_remote_code=True)
    if device.startswith("cuda"):
        model = model.to(device)
    model.eval()
    return tokenizer, model


def process_pdf_batches(pdf_path: str, out_path: str, model_path: str,
                        device: str = "cuda", batch_size: int = 6,
                        max_new_tokens: int = 320, paras_limit: int = 6, table_row_limit: int = 6):
    pdf_path = Path(pdf_path)
    out_path = Path(out_path)
    tokenizer, model = load_model_and_tokenizer(model_path, device=device)

    # Stage 1: deterministic extraction (fast, single pass)
    pages_raw = []  # list of (page_number, page_elems)
    t0 = time.time()
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        for i, page in enumerate(pdf.pages, start=1):
            page_elems = extract_page_elements_simple(page)
            pages_raw.append((i, page_elems))
            if i % 50 == 0:
                print(f"Extracted {i}/{total_pages} pages (deterministic extraction stage).")
    t1 = time.time()
    print(f"Stage 1 extraction done: {len(pages_raw)} pages in {t1 - t0:.1f}s")

    # Stage 2: LLM batching for summaries + structured JSON (faster than per-page calls)
    total = len(pages_raw)
    batches = []
    for i in range(0, total, batch_size):
        batch_entries = []
        for (page_number, page_elems) in pages_raw[i:i + batch_size]:
            raw_for_model = build_raw_for_model(page_elems, page_number, pdf_path.name,
                                               paras_limit=paras_limit, table_row_limit=table_row_limit)
            batch_entries.append(raw_for_model)
        batches.append(batch_entries)

    print(f"Created {len(batches)} batches (batch_size={batch_size}).")

    with open(out_path, "w", encoding="utf-8") as fout:
        processed_pages = 0
        for bi, batch in enumerate(batches, start=1):
            start_b = time.time()
            try:
                generated = generate_batch_json(tokenizer, model, batch, pdf_path.name, device,
                                                max_new_tokens=max_new_tokens, temperature=0.0)
                # parse generated JSON array into list
                parsed_list = json.loads(generated)
                # parsed_list should be list of page objects
                if not isinstance(parsed_list, list):
                    raise ValueError("Model did not return a JSON array")
            except Exception as e:
                # fallback: if model fails, generate simple deterministic enriched objects per page
                print(f"Warning: model batch {bi} failed to produce valid JSON: {e}")
                parsed_list = []
                for entry in batch:
                    page_num = entry["page_number"]
                    deterministic = {
                        "page_number": page_num,
                        "chunk_id": f"{pdf_path.name}_page_{page_num}",
                        "source_file": pdf_path.name,
                        "page_numbers": [page_num],
                        "headings": entry.get("headings", []),
                        "paragraphs": entry.get("paragraphs", []),
                        "tables": entry.get("tables", []),
                        "document_text": (" ".join(entry.get("paragraphs", [])[:2]) + " " + " ".join(entry.get("headings", [])[:2])).strip(),
                        "summary": "",
                        "important_entities": [],
                        "meta": {"ocr": False, "confidence": None},
                    }
                    parsed_list.append(deterministic)

            # Ensure parsed_list length matches batch length (map by page_number)
            parsed_by_page = {p["page_number"]: p for p in parsed_list if isinstance(p, dict) and p.get("page_number")}
            for entry in batch:
                pn = entry["page_number"]
                if pn in parsed_by_page:
                    out_obj = parsed_by_page[pn]
                else:
                    # fallback deterministic per-page object
                    out_obj = {
                        "page_number": pn,
                        "chunk_id": f"{pdf_path.name}_page_{pn}",
                        "source_file": pdf_path.name,
                        "page_numbers": [pn],
                        "headings": entry.get("headings", []),
                        "paragraphs": entry.get("paragraphs", []),
                        "tables": entry.get("tables", []),
                        "document_text": (" ".join(entry.get("paragraphs", [])[:2]) + " " + " ".join(entry.get("headings", [])[:2])).strip(),
                        "summary": "",
                        "important_entities": [],
                        "meta": {"ocr": False, "confidence": None},
                    }
                # Enforce minimal schema defaults
                out_obj.setdefault("chunk_id", f"{pdf_path.name}_page_{pn}")
                out_obj.setdefault("source_file", pdf_path.name)
                out_obj.setdefault("page_numbers", [pn])
                out_obj.setdefault("headings", [])
                out_obj.setdefault("paragraphs", [])
                out_obj.setdefault("tables", [])
                out_obj.setdefault("document_text", "")
                out_obj.setdefault("summary", "")
                out_obj.setdefault("important_entities", [])
                out_obj.setdefault("meta", {"ocr": False, "confidence": None})

                fout.write(json.dumps(out_obj, ensure_ascii=False) + "\n")
                processed_pages += 1

            end_b = time.time()
            print(f"Batch {bi}/{len(batches)} processed ({len(batch)} pages) in {end_b - start_b:.1f}s. Total pages processed: {processed_pages}/{total}")

    t2 = time.time()
    print(f"All done. Output written to {out_path}. Total time: {t2 - t0:.1f}s (extraction+LLM).")


# -----------------------------
# CLI
# -----------------------------


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Faster PDF -> RAFT JSONL using a local Llama model (GPU ready).")
    parser.add_argument("--pdf", required=True, help="Input PDF path")
    parser.add_argument("--out", required=True, help="Output JSONL path")
    parser.add_argument("--model_path", required=True, help="Local model directory (Llama3-8B-Instruct)")
    parser.add_argument("--device", default="cuda", choices=["cuda", "cpu"], help="Device for model")
    parser.add_argument("--batch_size", type=int, default=6, help="Number of pages per LLM batch (tune for GPU mem)")
    parser.add_argument("--max_new_tokens", type=int, default=320, help="max_new_tokens for generation (summary+entities)")
    parser.add_argument("--paras_limit", type=int, default=6, help="paragraphs per page to include in prompt")
    parser.add_argument("--table_row_limit", type=int, default=6, help="rows per table to include in prompt")
    args = parser.parse_args()

    start = time.time()
    process_pdf_batches(args.pdf, args.out, args.model_path,
                        device=args.device, batch_size=args.batch_size,
                        max_new_tokens=args.max_new_tokens,
                        paras_limit=args.paras_limit, table_row_limit=args.table_row_limit)
    print("Finished in {:.1f}s".format(time.time() - start))
