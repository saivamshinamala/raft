"""
pdf_to_jsonl_intelligent.py

Intelligent, GPU-accelerated PDF -> RAFT-friendly JSONL extraction using a local Llama model.
Goals:
 - Retain speed improvements (batching, deterministic fast extraction)
 - Add semantic intelligence: extract structured key-value facts, normalize numeric values/units,
   canonicalize table columns, infer section boundaries, list important entities, and generate
   RAFT-style instruction/response QA pairs for training.

Usage:
    python pdf_to_jsonl_intelligent.py --pdf "data/pdf/Shakti Userhand Book for Bot.pdf" --out data/pdf_chunks/output_intel.jsonl --model_path E:/Meta-Llama-3-8B-Instruct --device cuda --batch_size 4

Notes:
 - This script batches pages for the LLM to reduce per-call overhead.
 - It truncates long page content in prompts; adjust paras_limit/table_row_limit if you need more context.
 - The model is asked to output a strict JSON array. If parsing fails, a deterministic fallback is used.
 - For very large PDFs tune --batch_size and --max_new_tokens to fit GPU memory.
"""

import argparse
import json
import time
from pathlib import Path
from typing import List, Dict, Any

import pdfplumber
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# -----------------------------
# Deterministic extraction (fast)
# -----------------------------


def group_chars_to_lines(chars: List[Dict[str, Any]], y_tolerance: float = 3.0) -> List[Dict]:
    if not chars:
        return []
    chars = sorted(chars, key=lambda c: (round(c.get("top", 0)), c.get("x0", 0)))
    lines = []
    cur_top = chars[0]["top"]
    cur_chars = [chars[0]]
    for ch in chars[1:]:
        if abs(ch.get("top", 0) - cur_top) <= y_tolerance:
            cur_chars.append(ch)
        else:
            text = "".join(c.get("text", "") for c in cur_chars).strip()
            sizes = [c.get("size", 0) for c in cur_chars if "size" in c]
            size_mean = float(sum(sizes) / len(sizes)) if sizes else 0.0
            lines.append({"text": text, "top": cur_top, "size_mean": size_mean})
            cur_top = ch.get("top", 0)
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
                    obj = { (header[i] if i < len(header) and header[i] else f"col_{i+1}"): (r[i] if i < len(r) else "") for i in range(max(len(header), len(r))) }
                    structured_rows.append(obj)
            else:
                maxcols = max(len(r) for r in rows)
                header = [f"col_{i+1}" for i in range(maxcols)]
                for r in rows:
                    obj = {header[i]: (r[i] if i < len(r) else "") for i in range(maxcols)}
                    structured_rows.append(obj)
        tables.append({"rows": rows, "header": header, "structured_rows": structured_rows})
    return tables


def extract_page_elements(page) -> Dict[str, Any]:
    chars = getattr(page, "chars", []) or []
    lines = group_chars_to_lines(chars)
    headings = detect_headings(lines)

    raw_text = page.extract_text(x_tolerance=2) or ""
    paragraphs = [p.strip() for p in raw_text.split("\n\n") if p.strip()]
    if not paragraphs and lines:
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
# Intelligent prompt (batched)
# -----------------------------


INTELLIGENT_BATCH_PROMPT = """
You are a precise JSON-only extractor. Convert the following list of raw page objects (from a single PDF)
into a JSON array where each element is a fully structured page-level object for downstream retrieval and RAFT training.

Schema for each page (STRICT - use these keys):
{
  "page_number": int,
  "chunk_id": "<file>_page_<n>",
  "source_file": "<filename>",
  "page_numbers": [int],
  "sections": [ {"title": "<section title or null>", "start_paragraph": int, "end_paragraph": int} ],
  "key_values": [ {"key": "<name>", "value": "<original string>", "normalized_value": <number|null>, "unit": "<unit or null>", "confidence": "<low|med|high>"} ],
  "headings": [ "<strings>" ],
  "paragraphs": [ "<strings>" ],
  "tables": [ {
      "header": [ "<col names>" ] or null,
      "rows": [[cell,...],...],
      "structured_rows": [ {col: val, ...}, ... ],
      "normalized_columns": { "col_name": "number|string|date|percentage|unit" },
      "notes": "<short>"
  } ],
  "document_text": "<short concatenation useful for retrieval (<= 400 tokens)>",
  "summary": "<1-2 sentence summary>",
  "important_entities": ["ent1","ent2",... up to 8],
  "qa_pairs": [ {"instruction":"<short instruction>", "response":"<ground-truth answer from page>"} ],
  "meta": {"ocr": false, "confidence": null}
}

Requirements and guidance:
 - Output only valid JSON (a single JSON array).
 - For key_values: find explicit facts like Frequency Coverage, DF Accuracy, Quantities, Part Nos, ERP, etc.
   Parse numeric values and units into normalized_value and unit where possible. Use null if not parseable.
 - For tables: infer column types (normalized_columns) and parse numeric-like cells into numbers when obvious.
 - 'document_text' should be a concise (<=400 tokens) join of the most informative heading + first 2 paragraphs + table captions/first-row summary.
 - 'qa_pairs' should contain 1-3 high-quality instruction->answer examples per page that can be used directly for RAFT (e.g., "What is the frequency coverage?" -> "0.175 – 40 GHz").
 - Keep 'summary' to at most 2 sentences.
 - Keep 'important_entities' short tokens (section names, numbers, units, part nos).
 - Use confidence labels (low|med|high) for parsed numeric normalizations.

Now convert the following raw pages (they are small JSON objects with page_number, headings, paragraphs, tables, text_excerpt, source_file).
Return a JSON array as specified, one element per raw page exactly.
Do not include any extra commentary.
Raw pages:
{raw}
"""


def build_compact_for_prompt(page_elems: Dict[str, Any], page_number: int, source_file: str,
                             paras_limit: int = 8, table_row_limit: int = 5) -> Dict[str, Any]:
    # Keep essential info only (truncate long fields) to stay within prompt size.
    paras = page_elems.get("paragraphs", [])[:paras_limit]
    tables_sample = []
    for t in page_elems.get("tables", [])[:6]:
        rows = t.get("rows", [])[:table_row_limit]
        header = t.get("header")
        structured = t.get("structured_rows", [])[:table_row_limit]
        tables_sample.append({"header": header, "rows": rows, "structured_rows": structured})
    return {
        "page_number": page_number,
        "headings": page_elems.get("headings", [])[:6],
        "paragraphs": paras,
        "tables": tables_sample,
        "text_excerpt": (page_elems.get("raw_text") or "")[:3000],
        "source_file": source_file,
    }


def generate_intelligent_batch(tokenizer, model, batch_raw: List[Dict[str, Any]], device: str,
                               max_new_tokens: int = 512, temperature: float = 0.0) -> str:
    raw = json.dumps(batch_raw, ensure_ascii=False, separators=(",", ":"), indent=2)
    prompt = INTELLIGENT_BATCH_PROMPT.format(raw=raw)

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=4096 - max_new_tokens)
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)

    with torch.no_grad():
        out = model.generate(input_ids=input_ids,
                             attention_mask=attention_mask,
                             max_new_tokens=max_new_tokens,
                             temperature=temperature,
                             do_sample=False,
                             eos_token_id=tokenizer.eos_token_id,
                             pad_token_id=tokenizer.pad_token_id)
    gen = tokenizer.decode(out[0][input_ids.shape[-1]:], skip_special_tokens=True).strip()
    # extract JSON array substring if model adds fluff
    if "[" in gen and "]" in gen:
        start = gen.find("[")
        end = gen.rfind("]") + 1
        return gen[start:end]
    return gen


# -----------------------------
# Main pipeline
# -----------------------------


def load_model_and_tokenizer(model_path: str, device: str = "cuda"):
    dtype = torch.float16 if device.startswith("cuda") else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=dtype, trust_remote_code=True)
    if device.startswith("cuda"):
        model = model.to(device)
    model.eval()
    return tokenizer, model


def process_pdf_intelligent(pdf_path: str, out_path: str, model_path: str,
                            device: str = "cuda", batch_size: int = 4, max_new_tokens: int = 512,
                            paras_limit: int = 8, table_row_limit: int = 5):
    pdf_path = Path(pdf_path)
    out_path = Path(out_path)
    tokenizer, model = load_model_and_tokenizer(model_path, device=device)

    # Stage 1: fast deterministic extraction
    t0 = time.time()
    pages_raw = []
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages, start=1):
            page_elems = extract_page_elements(page)
            pages_raw.append((i, page_elems))
            if i % 50 == 0:
                print(f"Extracted {i}/{total} pages.")
    t1 = time.time()
    print(f"Deterministic extraction done: {len(pages_raw)} pages in {t1 - t0:.1f}s")

    # Stage 2: batch LLM intelligent extraction
    batches = []
    for i in range(0, len(pages_raw), batch_size):
        batch_entries = []
        for (pn, pe) in pages_raw[i:i + batch_size]:
            batch_entries.append(build_compact_for_prompt(pe, pn, pdf_path.name,
                                                         paras_limit=paras_limit, table_row_limit=table_row_limit))
        batches.append(batch_entries)

    print(f"Prepared {len(batches)} LLM batches (batch_size={batch_size}).")

    with open(out_path, "w", encoding="utf-8") as fout:
        processed = 0
        for bi, batch in enumerate(batches, start=1):
            start_b = time.time()
            try:
                generated = generate_intelligent_batch(tokenizer, model, batch, device,
                                                       max_new_tokens=max_new_tokens, temperature=0.0)
                parsed = json.loads(generated)
                if not isinstance(parsed, list):
                    raise ValueError("LLM did not return a JSON array")
            except Exception as e:
                # fallback deterministic enrichment (less intelligent but safe)
                print(f"Warning: LLM batch {bi} failed ({e}). Using deterministic fallback for this batch.")
                parsed = []
                for entry in batch:
                    pn = entry["page_number"]
                    deterministic = {
                        "page_number": pn,
                        "chunk_id": f"{pdf_path.name}_page_{pn}",
                        "source_file": pdf_path.name,
                        "page_numbers": [pn],
                        "sections": [],
                        "key_values": [],
                        "headings": entry.get("headings", []),
                        "paragraphs": entry.get("paragraphs", []),
                        "tables": entry.get("tables", []),
                        "document_text": (" ".join(entry.get("headings", [])[:1]) + " " + " ".join(entry.get("paragraphs", [])[:2])).strip(),
                        "summary": "",
                        "important_entities": [],
                        "qa_pairs": [],
                        "meta": {"ocr": False, "confidence": None},
                    }
                    parsed.append(deterministic)

            # Write one JSON object per page (jsonl)
            # Map by page_number to preserve ordering
            parsed_map = {p.get("page_number"): p for p in parsed if isinstance(p, dict) and p.get("page_number") is not None}
            for entry in batch:
                pn = entry["page_number"]
                out_obj = parsed_map.get(pn)
                if not out_obj:
                    # defensive fallback if LLM skipped a page
                    out_obj = {
                        "page_number": pn,
                        "chunk_id": f"{pdf_path.name}_page_{pn}",
                        "source_file": pdf_path.name,
                        "page_numbers": [pn],
                        "sections": [],
                        "key_values": [],
                        "headings": entry.get("headings", []),
                        "paragraphs": entry.get("paragraphs", []),
                        "tables": entry.get("tables", []),
                        "document_text": (" ".join(entry.get("headings", [])[:1]) + " " + " ".join(entry.get("paragraphs", [])[:2])).strip(),
                        "summary": "",
                        "important_entities": [],
                        "qa_pairs": [],
                        "meta": {"ocr": False, "confidence": None},
                    }
                # ensure schema completeness
                out_obj.setdefault("chunk_id", f"{pdf_path.name}_page_{pn}")
                out_obj.setdefault("source_file", pdf_path.name)
                out_obj.setdefault("page_numbers", [pn])
                out_obj.setdefault("sections", [])
                out_obj.setdefault("key_values", [])
                out_obj.setdefault("headings", [])
                out_obj.setdefault("paragraphs", [])
                out_obj.setdefault("tables", [])
                out_obj.setdefault("document_text", "")
                out_obj.setdefault("summary", "")
                out_obj.setdefault("important_entities", [])
                out_obj.setdefault("qa_pairs", [])
                out_obj.setdefault("meta", {"ocr": False, "confidence": None})

                fout.write(json.dumps(out_obj, ensure_ascii=False) + "\n")
                processed += 1

            end_b = time.time()
            print(f"Batch {bi}/{len(batches)} processed ({len(batch)} pages) in {end_b - start_b:.1f}s. Total: {processed}/{len(pages_raw)}")

    t2 = time.time()
    print(f"Finished. Output written to {out_path}. Total elapsed: {t2 - t0:.1f}s")


# -----------------------------
# CLI
# -----------------------------


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Intelligent PDF -> RAFT JSONL using local Llama (GPU recommended).")
    parser.add_argument("--pdf", required=True, help="Input PDF")
    parser.add_argument("--out", required=True, help="Output JSONL file")
    parser.add_argument("--model_path", required=True, help="Local model directory (Llama3-8B-Instruct)")
    parser.add_argument("--device", default="cuda", choices=["cuda", "cpu"], help="Device for model")
    parser.add_argument("--batch_size", type=int, default=4, help="Pages per LLM batch (tune for GPU memory)")
    parser.add_argument("--max_new_tokens", type=int, default=512, help="LLM max_new_tokens (summary+QA+normalization)")
    parser.add_argument("--paras_limit", type=int, default=8, help="Paragraphs per page to include in prompt")
    parser.add_argument("--table_row_limit", type=int, default=5, help="Rows per table to include in prompt")
    args = parser.parse_args()

    start_time = time.time()
    process_pdf_intelligent(args.pdf, args.out, args.model_path,
                            device=args.device, batch_size=args.batch_size,
                            max_new_tokens=args.max_new_tokens,
                            paras_limit=args.paras_limit, table_row_limit=args.table_row_limit)
    print("Total runtime: {:.1f}s".format(time.time() - start_time))