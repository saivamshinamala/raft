#!/usr/bin/env python3
"""
Intelligent PDF extractor + LLM-based canonicalizer for RAG-friendly chunks.

Usage (example):
  from transformers import pipeline
  llm = pipeline("text-generation", model="path/to/llama-3-8b-instruct", device_map="auto", return_full_text=False)
  run_pdf_to_chunks("data/pdf/Shakti Userhand Book for Bot.pdf", llm, out_jsonl="data/pdf_chunks/clean_chunks.jsonl")

Notes:
- Requires: pdfplumber, pytesseract (optional), transformers (or any LLM pipeline callable with signature llm(prompt, **kwargs)).
- The LLM function must accept a prompt and return text that is JSON (see prompts below).
- Target chunk size in words is configurable (default 400 with 60 overlap).
"""

import json
import os
import re
import uuid
from typing import List, Dict, Any, Optional
import pdfplumber
try:
    import pytesseract
    from PIL import Image
    HAVE_OCR = True
except Exception:
    HAVE_OCR = False

# --- USER ADJUSTABLE ---
REPLACEMENTS = {
    "CONFIDENTIAL": "",
    "EW": "Electronic Warfare",
    "SCD": "System Controller and Display",
    "ESMP": "Electronic Support Measures Processor",
    "ESM": "Electronic Support Measures",
    "ESI": "External System Interface",
    "ES": "Electronic Support",
    "RFPS": "Radar Finger Printing System",
    "EA": "Electronic Attack",
    "ECM": "Electronic Counter Measures",
    "CMS": "Combat Management System",
    "NBRx1": "Narrow Band Receiver 1",
    "NBRx2": "Narrow Band Receiver 2",
    "BBRx1": "Broad Band Receiver 1",
    "BBRx2": "Broad Band Receiver 2",
    "NBRx": "Narrow Band Receiver",
    "BBRx": "Broad Band Receiver"
}

TARGET_CHUNK_WORDS = 400
OVERLAP_WORDS = 60
LLM_MAX_TOKENS = 512  # for canonicalizer responses (tune if needed)
LLM_TEMPERATURE = 0.0

# --- Helpers ---
def replace_acronyms(text: str) -> str:
    if not REPLACEMENTS:
        return text
    pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in REPLACEMENTS.keys()) + r')\b')
    return pattern.sub(lambda m: REPLACEMENTS[m.group()], text)

def table_to_markdown(table: List[List[Any]]) -> str:
    if not table:
        return ""
    # Take first row as header (if looks header-ish)
    headers = [str(c).strip() if c is not None else "" for c in table[0]]
    rows = [[str(c).strip() if c is not None else "" for c in r] for r in table[1:]]
    # compute col widths
    cols = [headers] + rows
    col_widths = [max(len(row[i]) if i < len(row) else 0 for row in cols) for i in range(len(headers))]
    md = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |\n"
    md += "| " + " | ".join("-" * col_widths[i] for i in range(len(headers))) + " |\n"
    for r in rows:
        md += "| " + " | ".join((r[i] if i < len(r) else "").ljust(col_widths[i]) for i in range(len(headers))) + " |\n"
    return md

def words(text: str) -> int:
    return len(re.findall(r'\w+', text))

# --- Structural extraction ---
def extract_structured_pdf(pdf_path: str) -> List[Dict[str, Any]]:
    """
    Returns list of segments: dictionaries with
      - id
      - source_file
      - page (1-indexed)
      - type: 'text' | 'table' | 'figure'
      - text
      - bbox (optional)
    """
    segments = []
    header_footer_candidates = {}
    with pdfplumber.open(pdf_path) as pdf:
        # Collect first/last line frequencies for header/footer removal
        for i, page in enumerate(pdf.pages[:30]):  # sample first 30 pages to detect repeating headers
            txt = page.extract_text() or ""
            lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
            if lines:
                header_footer_candidates[lines[0]] = header_footer_candidates.get(lines[0], 0) + 1
                header_footer_candidates[lines[-1]] = header_footer_candidates.get(lines[-1], 0) + 1

        # define header/footer lines that occur in many pages ( > 5 pages threshold )
        repeated = {line for line, c in header_footer_candidates.items() if c >= 5}

        for pno, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text() or ""
            # remove header/footer lines that repeat
            lines = [ln for ln in page_text.splitlines()]
            cleaned_lines = [ln for ln in lines if ln.strip() and ln.strip() not in repeated]
            cleaned_text = "\n".join(cleaned_lines).strip()

            # Basic cleaning
            cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
            if cleaned_text:
                segments.append({
                    "id": f"{os.path.basename(pdf_path)}:p{pno}:t",
                    "source_file": os.path.basename(pdf_path),
                    "start_page": pno,
                    "end_page": pno,
                    "is_table": False,
                    "type": "text",
                    "text": cleaned_text
                })

            # Extract tables
            try:
                tables = page.extract_tables()
            except Exception:
                tables = []
            for ti, tbl in enumerate(tables, start=1):
                md = table_to_markdown(tbl)
                if md.strip():
                    segments.append({
                        "id": f"{os.path.basename(pdf_path)}:p{pno}:table{ti}",
                        "source_file": os.path.basename(pdf_path),
                        "start_page": pno,
                        "end_page": pno,
                        "is_table": True,
                        "type": "table",
                        "text": md
                    })

            # Extract simple images and do OCR if available
            if HAVE_OCR:
                for img_idx, img in enumerate(page.images or []):
                    try:
                        bbox = (img["x0"], img["top"], img["x1"], img["bottom"])
                        with page.crop(bbox) as r:
                            pil = r.to_image(resolution=150).original
                            ocr_text = pytesseract.image_to_string(pil)
                            if ocr_text and ocr_text.strip():
                                segments.append({
                                    "id": f"{os.path.basename(pdf_path)}:p{pno}:img{img_idx}",
                                    "source_file": os.path.basename(pdf_path),
                                    "start_page": pno,
                                    "end_page": pno,
                                    "is_table": False,
                                    "type": "figure",
                                    "text": "[FIGURE OCR]\n" + ocr_text.strip()
                                })
                    except Exception:
                        continue
            else:
                # collect image presence as placeholder
                if page.images:
                    segments.append({
                        "id": f"{os.path.basename(pdf_path)}:p{pno}:img_info",
                        "source_file": os.path.basename(pdf_path),
                        "start_page": pno,
                        "end_page": pno,
                        "is_table": False,
                        "type": "figure",
                        "text": f"[{len(page.images)} images present on page {pno} — OCR disabled]"
                    })

    return segments

# --- LLM canonicalizer ---
LLM_PROMPT_TEMPLATE = """
You are a JSON-outputting cleaner and summarizer. Input: a piece of extracted PDF content (text, table markdown or OCR output) with source page metadata.
Task:
- Clean header/footer noise and normalize common acronyms (e.g., replace EW -> Electronic Warfare).
- If input is a table (markdown), keep it as markdown and create a short textual summary of the table.
- Produce:
  1) "title" : a short descriptive title (5-10 words)
  2) "chunk_text" : cleaned, canonicalized text ready for vectorization; keep tables as markdown inside; limit to approximately {target_words} words (do not invent facts)
  3) "tags": short list of keywords (3-8)
  4) "highlights": 3-6 bullet key facts
  5) "start_page" and "end_page" copied as provided
Return ONLY a JSON object (no extra prose). Input follows, delimited by =====.

METADATA: {meta_json}

=====
{content}
=====
Remember: be concise, factual, do not hallucinate, and preserve tables as markdown.
"""

def call_llm_canonicalizer(llm_callable, content: str, meta: Dict[str, Any], target_words=TARGET_CHUNK_WORDS) -> Dict[str, Any]:
    prompt = LLM_PROMPT_TEMPLATE.format(target_words=target_words, meta_json=json.dumps(meta), content=content)
    # llm_callable is a pipeline-like object: llm_callable(prompt, max_new_tokens=..., temperature=...)
    resp = llm_callable(prompt, max_new_tokens=LLM_MAX_TOKENS, temperature=LLM_TEMPERATURE)
    # The pipeline might return a list of dicts or a string; handle both
    if isinstance(resp, list):
        text_out = resp[0].get("generated_text") or resp[0].get("text") or str(resp[0])
    else:
        text_out = str(resp)

    # Try to extract a JSON substring
    json_text = None
    try:
        # Find first { and last }
        start = text_out.find('{')
        end = text_out.rfind('}')
        if start != -1 and end != -1:
            candidate = text_out[start:end+1]
            json_text = json.loads(candidate)
    except Exception:
        json_text = None

    if not json_text:
        # Fallback: create conservative output
        json_text = {
            "title": (content[:80].split(".")[0]).strip(),
            "chunk_text": replace_acronyms(re.sub(r'\s+', ' ', content).strip())[:target_words*6],  # naive
            "tags": [],
            "highlights": [],
            "start_page": meta.get("start_page"),
            "end_page": meta.get("end_page")
        }
    return json_text

# --- Merge/Finalize into word-sized chunks with overlap ---
def assemble_chunks(canonical_segments: List[Dict[str, Any]], target_words=TARGET_CHUNK_WORDS, overlap=OVERLAP_WORDS) -> List[Dict[str, Any]]:
    """
    canonical_segments: each has 'chunk_text', 'title', 'start_page', 'end_page', 'tags', 'highlights'
    Returns final chunks (with overlap).
    """
    out_chunks = []
    buffer_text = ""
    buffer_meta = {"start_page": None, "end_page": None, "source_file": None, "components": []}

    def flush_buffer():
        nonlocal buffer_text, buffer_meta
        if not buffer_text.strip():
            return
        # create id
        cid = str(uuid.uuid4())
        chunk_words = words(buffer_text)
        out_chunks.append({
            "id": cid,
            "title": buffer_meta.get("title") or buffer_text[:80],
            "source_file": buffer_meta.get("source_file"),
            "start_page": buffer_meta.get("start_page"),
            "end_page": buffer_meta.get("end_page"),
            "is_table": False,
            "text": buffer_text.strip(),
            "word_count": chunk_words,
            "components": buffer_meta.get("components", [])
        })
        # prepare overlap
        tokens = buffer_text.split()
        if len(tokens) > overlap:
            buffer_text = " ".join(tokens[-overlap:])
        else:
            buffer_text = ""
        buffer_meta = {"start_page": None, "end_page": None, "source_file": buffer_meta.get("source_file"), "components": []}

    for seg in canonical_segments:
        txt = seg.get("chunk_text", "").strip()
        if not txt:
            continue
        if buffer_meta["start_page"] is None:
            buffer_meta["start_page"] = seg.get("start_page")
        buffer_meta["end_page"] = seg.get("end_page")
        if not buffer_meta.get("source_file"):
            buffer_meta["source_file"] = seg.get("source_file")
        buffer_text = (buffer_text + " " + txt).strip()
        buffer_meta.setdefault("components", []).append({"title": seg.get("title"), "start_page": seg.get("start_page"), "end_page": seg.get("end_page")})
        if words(buffer_text) >= target_words:
            # compute composite title
            buffer_meta["title"] = seg.get("title") or buffer_meta["components"][0]["title"]
            flush_buffer()

    # flush remainder
    flush_buffer()
    return out_chunks

# --- Public runner ---
def run_pdf_to_chunks(pdf_path: str, llm_callable, out_jsonl: str, target_words=TARGET_CHUNK_WORDS, overlap=OVERLAP_WORDS):
    # 1) structural extraction
    print(f"[1/3] Extracting structured segments from {pdf_path}...")
    segments = extract_structured_pdf(pdf_path)
    print(f"  -> extracted {len(segments)} raw segments")

    # 2) canonicalize each segment with LLM
    print("[2/3] Canonicalizing segments with LLM...")
    canonicalized = []
    for i, s in enumerate(segments, start=1):
        meta = {"start_page": s["start_page"], "end_page": s["end_page"], "type": s["type"], "id": s["id"], "source_file": s["source_file"]}
        try:
            out = call_llm_canonicalizer(llm_callable, s["text"], meta, target_words=target_words)
            out.update({"source_file": s["source_file"], "start_page": s["start_page"], "end_page": s["end_page"]})
            canonicalized.append(out)
        except Exception as e:
            print(f"   ! LLM canonicalization failed for segment {s['id']}: {e}")
            # fallback simple canonicalization
            fallback = {
                "title": (s["text"][:60].split(".")[0]),
                "chunk_text": replace_acronyms(s["text"]),
                "tags": [],
                "highlights": [],
                "start_page": s["start_page"],
                "end_page": s["end_page"],
                "source_file": s["source_file"]
            }
            canonicalized.append(fallback)
        if i % 50 == 0:
            print(f"   canonicalized {i}/{len(segments)}")

    print(f"  -> canonicalized {len(canonicalized)} segments")

    # 3) assemble final chunks (merge segments up to target word size with overlap)
    print("[3/3] Assembling final chunks with overlap...")
    final_chunks = assemble_chunks(canonicalized, target_words=target_words, overlap=overlap)
    print(f"  -> produced {len(final_chunks)} chunks")

    # write jsonl
    print(f"Writing chunks to {out_jsonl} ...")
    with open(out_jsonl, "w", encoding="utf-8") as f:
        for c in final_chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print("Done.")
    return final_chunks

# If invoked directly, provide a tiny CLI (requires an LLM pipeline to be provided by caller)
if __name__ == "__main__":
    # run_pdf_to_chunks("data\pdf\Shakti Userhand Book for Bot.pdf", "E:/Meta-Llama-3-8B-Instruct", "data/pdf/ai_pdf_chunks/chunks.jsonl")
    print("This module contains functions; import and call run_pdf_to_chunks(pdf_path, llm_callable, out_jsonl).")