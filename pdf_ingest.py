#!/usr/bin/env python3
"""
pdf_structured_ingest.py

Usage:
    python pdf_structured_ingest.py --pdf path/to/file.pdf --out chunks.jsonl \
        [--min_words 120 --max_words 450 --overlap_words 60] [--llm_model PATH_OR_NAME]

Produces a structured chunks.jsonl with fields:
  id, source_file, start_page, end_page, is_table, table_md, table_csv,
  images, section, text, summary (optional LLM), words
"""

import pdfplumber
import re
import json
import uuid
import argparse
from pathlib import Path
from datetime import datetime
from itertools import chain
import html
import csv
import os

# Optional LLM imports (commented out if you don't want to run LLM postprocess)
from transformers import pipeline

# ==== Config ====
HEADER_FOOTER_PATTERNS = [
    r"SHAKTI\s*:\s*UHB\\Ch\d+\s+Page\s+\d+\s+of\s+\d+",      # your example header
    r"CONFIDENTIAL",
    r"Page\s+\d+\s+of\s+\d+",
]

# A light cleaning regex to canonicalize whitespace and remove weird unicode
def clean_text_block(s: str) -> str:
    if not s:
        return ""
    s = html.unescape(s)
    s = s.replace("\r", " ").replace("\n", " ").strip()
    # remove multiple spaces
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def remove_headers_footers(text: str):
    for p in HEADER_FOOTER_PATTERNS:
        text = re.sub(p, " ", text, flags=re.IGNORECASE)
    # remove leading/trailing page artifacts like "This page is intentionally left blank"
    text = re.sub(r"This page is intentionally left blank", " ", text, flags=re.I)
    return clean_text_block(text)

def table_to_markdown(table):
    # table: list of lists, first row may be header
    if not table:
        return ""
    # ensure str and strip
    table = [[("" if c is None else str(c)).strip() for c in row] for row in table]
    header = table[0]
    rows = table[1:] if len(table) > 1 else []
    # column widths
    cols = list(zip(header, *rows)) if rows else [(h,) for h in header]
    widths = [max(len(cell) for cell in col) for col in cols]
    md = "| " + " | ".join(h.ljust(w) for h, w in zip(header, widths)) + " |\n"
    md += "| " + " | ".join("-" * w for w in widths) + " |\n"
    for r in rows:
        md += "| " + " | ".join((r[i] if i < len(r) else "").ljust(widths[i]) for i in range(len(header))) + " |\n"
    return md

def write_table_csv(table, out_path: Path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for row in table:
            w.writerow([("" if c is None else str(c)).strip() for c in row])

# Very simple heuristic to detect heading lines
def is_heading_line(line: str) -> bool:
    line = line.strip()
    if not line:
        return False
    if re.match(r'^[0-9]+(\.[0-9]+)*\s+', line):  # 1.2 or 1.2.3
        return True
    # ALL CAPS (short)
    if line.isupper() and 2 < len(line.split()) < 8:
        return True
    # words like "Figure" or "Table" are headings/captions
    if re.match(r'^(Figure|Fig\.|Table|TABLE)\b', line, re.I):
        return True
    return False

def split_sentences(text: str):
    # light sentence split - you can swap for nltk.sent_tokenize if available
    sents = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sents if s.strip()]

def semantic_chunker(paragraphs, min_words=120, max_words=450, overlap_words=60):
    """
    paragraphs: list of (section_heading_or_none, text)
    returns list of chunks dicts: {text, section}
    """
    chunks = []
    buffer_text = []
    buffer_words = 0
    current_section = None

    def flush_buffer():
        nonlocal buffer_text, buffer_words, current_section
        if buffer_text:
            txt = " ".join(buffer_text).strip()
            chunks.append({"text": txt, "section": current_section, "words": len(txt.split())})
            # overlap seeding
            if overlap_words > 0:
                words = txt.split()
                buffer_text = [" ".join(words[-overlap_words:])] if len(words) >= overlap_words else buffer_text[-1:]
                buffer_words = len(buffer_text[0].split())
            else:
                buffer_text = []
                buffer_words = 0

    for section, para in paragraphs:
        if section:
            # if we have content and new section, flush to keep section boundaries
            if buffer_text:
                flush_buffer()
            current_section = section
        # split paragraph into sentences for stable chunking
        sents = split_sentences(para)
        for s in sents:
            w = len(s.split())
            if buffer_words + w > max_words:
                # flush and start new
                flush_buffer()
                buffer_text = [s]
                buffer_words = w
            else:
                buffer_text.append(s)
                buffer_words += w
            # small-chunk early flush
            if buffer_words >= min_words:
                flush_buffer()
    # final flush
    if buffer_text:
        flush_buffer()
    return chunks

def extract_structured_chunks(pdf_path: str, out_jsonl: str,
                              min_words=120, max_words=450, overlap_words=60,
                              llm_model: str = None):
    pdf_path = Path(pdf_path)
    out_jsonl = Path(out_jsonl)
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)

    # Optional LLM summary pipeline
    llm_summarizer = None
    if llm_model:
        try:
            llm_summarizer = pipeline("text2text-generation", model=llm_model, device=0)
            print("[INFO] LLM summarizer loaded:", llm_model)
        except Exception as e:
            print("[WARN] Could not load LLM summarizer:", e)
            llm_summarizer = None

    id_counter = 0
    with pdfplumber.open(str(pdf_path)) as pdf, open(out_jsonl, "w", encoding="utf-8") as out_f:
        all_paragraphs = []  # list of (section, paragraph_text, start_page, end_page, tables, images)
        for pno, page in enumerate(pdf.pages, start=1):
            # extract text
            raw_text = page.extract_text() or ""
            raw_text = remove_headers_footers(raw_text)
            if not raw_text.strip():
                continue

            # extract tables
            tables = page.extract_tables() or []
            table_entries = []
            for ti, table in enumerate(tables, start=1):
                md = table_to_markdown(table)
                csv_name = f"{pdf_path.stem}_p{pno}_t{ti}.csv"
                csv_path = out_jsonl.parent / "tables" / csv_name
                csv_path.parent.mkdir(parents=True, exist_ok=True)
                write_table_csv(table, csv_path)
                table_entries.append({"table_md": md, "table_csv": str(csv_path), "page": pno})

            # images
            images = page.images or []
            saved_images = []
            if images:
                img_dir = out_jsonl.parent / "images"
                img_dir.mkdir(parents=True, exist_ok=True)
                for i, img in enumerate(images):
                    # you can crop and save image bytes via page.crop and page.to_image if desired
                    saved_images.append({"bbox": img, "note": "image detected on page", "page": pno})

            # Attempt to split into heading + paragraphs using simple heuristics
            lines = [ln.strip() for ln in (raw_text or "").splitlines() if ln.strip()]
            current_section = None
            buff_para = []
            for ln in lines:
                if is_heading_line(ln):
                    # flush existing para
                    if buff_para:
                        all_paragraphs.append((current_section, " ".join(buff_para)))
                        buff_para = []
                    # start new section
                    current_section = ln
                else:
                    buff_para.append(ln)
            if buff_para:
                all_paragraphs.append((current_section, " ".join(buff_para)))

        # Now chunk semantically
        chunks = semantic_chunker(all_paragraphs, min_words=min_words, max_words=max_words, overlap_words=overlap_words)

        # Optional LLM summaries for each chunk (short)
        for ch in chunks:
            id_counter += 1
            chunk_id = f"{pdf_path.name}:chunk:{id_counter:06d}"
            ch_text = ch["text"]
            ch_section = ch.get("section")
            summary = None
            if llm_summarizer:
                try:
                    prompt = f"Summarize the following in 1-2 sentences and give a short title:\n\n{ch_text}\n\nReturn JSON with keys: title, summary."
                    resp = llm_summarizer(prompt, max_new_tokens=150)
                    # naive parse of response
                    out = resp[0]["generated_text"].strip()
                    # try to split into title + summary heuristically
                    if "\n" in out:
                        title, summary = out.split("\n", 1)
                    else:
                        summary = out
                except Exception as e:
                    print("[WARN] LLM summarization failed:", e)
            out_obj = {
                "id": chunk_id,
                "source_file": str(pdf_path.name),
                "start_page": None,
                "end_page": None,
                "is_table": False,
                "table_md": None,
                "table_csv": None,
                "images": [],
                "section": ch_section,
                "text": ch_text,
                "summary": summary,
                "words": ch.get("words", len(ch_text.split())),
                "created_at": datetime.utcnow().isoformat() + "Z"
            }
            out_f.write(json.dumps(out_obj, ensure_ascii=False) + "\n")
    print(f"[ingest] Wrote structured chunks -> {out_jsonl} (approx {id_counter} chunks)")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--min_words", type=int, default=120)
    ap.add_argument("--max_words", type=int, default=450)
    ap.add_argument("--overlap_words", type=int, default=60)
    ap.add_argument("--llm_model", default=None)
    args = ap.parse_args()
    extract_structured_chunks(args.pdf, args.out,
                              min_words=args.min_words, max_words=args.max_words, overlap_words=args.overlap_words,
                              llm_model=args.llm_model)