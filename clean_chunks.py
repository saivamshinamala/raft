#!/usr/bin/env python3
"""
Post-process clean_chunks.jsonl -> clean_chunks_improved.jsonl

Goals:
- Merge very short adjacent segments into coherent chunks
- Detect and stitch table fragments into table chunks (is_table=True)
- Normalize/remove noisy titles (e.g. "2", "| 5", "| Ser ...")
- Optionally call an LLM pipeline to generate better titles, summaries, tags
- Output improved JSONL for indexing/fine-tuning

Usage:
  python pdf_ai_chunker_improved.py --in data/ai_pdf_chunks/clean_chunks.jsonl --out data/ai_pdf_chunks/clean_chunks_improved.jsonl \
      [--llm_model path_or_hf_id]

Notes:
- Requires: transformers (optional if you use LLM), but otherwise runs heuristics-only.
- The script expects input file entries with fields: id, title, source_file, start_page, end_page, is_table (optional), text (optional)
"""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
import uuid

# Optional LLM
try:
    from transformers import pipeline
    HAVE_TRANSFORMERS = True
except Exception:
    HAVE_TRANSFORMERS = False

# Heuristics
MIN_WORDS_TO_BE_SELF_CONTAINED = 40
MERGE_MAX_WORDS = 200  # if two adjacent fragments small, merge them up to this threshold
TARGET_CHUNK_WORDS = 400
OVERLAP_WORDS = 60

TABLE_LINE_SCORE_THRESHOLD = 0.6
TABLE_PIPELINE_MIN_COLS = 2

# Patterns that generally indicate bad titles / headers / page markers
BAD_TITLE_RE = re.compile(r'^(?:\||\d{1,3}$|page\s*\d+|^\s*$|^CHAPT|FIGURE|TABLE|^Page\b)', re.I)
REPEATED_PUNCT_RE = re.compile(r'^[\|\-\. ]+$')
MULTI_COL_PIPE = re.compile(r'\|')  # common in extracted tables
SEPARATOR_LINE = re.compile(r'^\s*[-=]{3,}\s*$')

# Utilities
def words(text: str) -> int:
    return len(re.findall(r'\w+', text or ""))

def is_bad_title(t: str) -> bool:
    if not t:
        return True
    t = t.strip()
    if not t:
        return True
    if REPEATED_PUNCT_RE.match(t):
        return True
    if BAD_TITLE_RE.match(t):
        # filter some false positives by length
        if len(t) < 8:
            return True
    # titles like "| Ser |" or single-column fragments
    if t.count('|') > 0 and len(t.split()) < 6:
        return True
    return False

def looks_like_table_text(text: str) -> bool:
    """
    Heuristic to detect if a text block is a fragment of a table
    - contains pipe separators OR
    - many short columns separated by multiple spaces, or rows with similar number of columns
    """
    if not text:
        return False
    # If already flagged by source is_table True, return True quickly
    if '\n' in text:
        lines = [ln for ln in text.splitlines() if ln.strip()]
    else:
        lines = [text]
    # Score pipes
    pipe_count = sum(1 for ln in lines if '|' in ln)
    if pipe_count / max(1, len(lines)) >= TABLE_LINE_SCORE_THRESHOLD:
        return True
    # Count columns by whitespace splitting for each line - if consistent and >=2, might be table
    col_counts = []
    for ln in lines:
        cols = re.split(r'\s{2,}', ln.strip())
        if len(cols) >= TABLE_PIPELINE_MIN_COLS:
            col_counts.append(len(cols))
    if not col_counts:
        return False
    # If most lines have at least 2 columns and similar counts, it's likely a table
    avg = sum(col_counts) / len(col_counts)
    if avg >= TABLE_PIPELINE_MIN_COLS and (max(col_counts)-min(col_counts) <= 2):
        return True
    return False

# LLM prompts for title generation / canonicalization
TITLE_PROMPT = """Create a short descriptive title (6 words max) for this document excerpt.
Do not invent facts; use only the content provided.

EXCERPT:
\"\"\"{excerpt}\"\"\"

Return only the title on a single line.
"""

CANONICALIZE_PROMPT = """You are a conservative cleaner. Given the excerpt below:
- Remove headers/footers (page markers, repeated "CONFIDENTIAL")
- Normalize known acronyms (do not invent new expansions)
- Return a cleaned paragraph (no lists or tables unless absolutely necessary)
Return JSON: {{ "title": "<short title>", "cleaned": "<cleaned text (one paragraph)>" }}
EXCERPT:
\"\"\"{excerpt}\"\"\"
"""

def load_chunks(path: Path) -> List[Dict[str, Any]]:
    arr = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                arr.append(obj)
            except Exception as e:
                print("Skipping invalid JSON line:", e, file=sys.stderr)
    return arr

def group_by_pages(chunks: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    # Group by source_file to do merges per-document
    out = {}
    for c in chunks:
        k = c.get("source_file", "unknown")
        out.setdefault(k, []).append(c)
    # sort each group by start_page, then by id
    for k in out:
        out[k].sort(key=lambda x: (x.get("start_page", 0) or 0, x.get("end_page", 0) or 0))
    return out

def stitch_tables_and_fix_titles(group: List[Dict[str, Any]], llm=None) -> List[Dict[str, Any]]:
    """
    Process a list of segments from same source_file.
    Steps:
      - Merge adjacent small segments (word count below threshold or same page neighbors)
      - Detect table fragments and stitch into one table chunk
      - Replace bad titles using LLM if available, else heuristics
    """
    out = []
    i = 0
    n = len(group)
    while i < n:
        seg = dict(group[i])  # shallow copy
        seg_text = seg.get("text", "") or ""
        seg_words = words(seg_text)
        seg_is_table = bool(seg.get("is_table", False)) or looks_like_table_text(seg_text)
        seg_title = seg.get("title", "") or ""
        # If segment is a very small piece, try to merge with next if same page or next small
        if seg_words < MIN_WORDS_TO_BE_SELF_CONTAINED and i+1 < n:
            # try to merge into a larger neighbor until threshold or limit
            merged = dict(seg)
            j = i+1
            while j < n and words(merged.get("text","")) < MERGE_MAX_WORDS:
                # only merge if contiguous pages or same small group
                next_seg = group[j]
                # break if next_seg starts beyond a gap of >2 pages to avoid wrong merges
                if (next_seg.get("start_page") or 0) - (merged.get("end_page") or 0) > 2:
                    break
                # merge text and adjust end_page
                merged_text = (merged.get("text","") or "") + "\n\n" + (next_seg.get("text","") or "")
                merged["text"] = merged_text
                merged["end_page"] = next_seg.get("end_page", merged.get("end_page"))
                merged["is_table"] = merged.get("is_table", False) or bool(next_seg.get("is_table", False)) or looks_like_table_text(merged_text)
                j += 1
            # if we merged at least one, use merged and skip those
            if j > i+1:
                seg = merged
                i = j  # continue after merged block
            else:
                i += 1
        else:
            i += 1

        # Now handle tables: if seg looks like table, try to aggregate neighboring table-like fragments into one
        if looks_like_table_text(seg.get("text","")):
            # collect following fragments that are also table-like on same page(s)
            pagespan_start = seg.get("start_page")
            pagespan_end = seg.get("end_page")
            collected_text = seg.get("text","")
            k = len(out)  # position if needed
            # check next items in group (we may have advanced i)
            # we look ahead in group to stitch small table fragments that overlap pages
            # simple approach: gather next up to 3 neighbors if table-like and contiguous pages
            lookahead_idx = None
            # find current index in original group to continue lookahead
            try:
                cur_idx = group.index(seg)
            except ValueError:
                cur_idx = None
            if cur_idx is None:
                # fallback: append seg as table chunk
                pass
            else:
                j = cur_idx + 1
                while j < n and j < cur_idx + 6:
                    candidate = group[j]
                    if looks_like_table_text(candidate.get("text","")) and (candidate.get("start_page",0) - pagespan_end) <= 1:
                        collected_text += "\n" + candidate.get("text","")
                        pagespan_end = max(pagespan_end, candidate.get("end_page", pagespan_end))
                        j += 1
                        # mark these as consumed by replacing them with empty text to avoid double-processing
                        group[j-1]["_consumed"] = True
                    else:
                        break
            seg["text"] = collected_text
            seg["start_page"] = pagespan_start
            seg["end_page"] = pagespan_end
            seg["is_table"] = True

        # Normalize title: if bad title generate via LLM or fallback heuristics
        if is_bad_title(seg_title):
            # build a candidate title from the text: extract first heading-like line or first sentence
            candidate_title = None
            # find first line that looks heading-ish (short and not a table row)
            for ln in (seg.get("text","") or "").splitlines():
                if ln.strip() and len(ln.strip()) <= 120 and len(ln.split()) <= 10:
                    if not looks_like_table_text(ln):
                        candidate_title = ln.strip()
                        break
            if not candidate_title:
                # take first sentence fallback
                m = re.search(r'(.{20,120}?[\.!?])\s', seg.get("text","") + " ")
                if m:
                    candidate_title = m.group(1).strip()
            # if LLM available, ask it to refine
            if candidate_title and (HAVE_TRANSFORMERS and llm is not None):
                try:
                    prompt = TITLE_PROMPT.format(excerpt=(candidate_title if len(candidate_title) < 200 else candidate_title[:200]))
                    out = llm(prompt, max_new_tokens=32, temperature=0.0)
                    if isinstance(out, list):
                        gen = (out[0].get("generated_text") or out[0].get("text") or "").strip()
                    else:
                        gen = str(out).strip()
                    if gen:
                        seg["title"] = re.sub(r'\s+', ' ', gen).strip()[:120]
                    else:
                        seg["title"] = candidate_title.strip()[:120]
                except Exception:
                    seg["title"] = candidate_title.strip()[:120]
            else:
                seg["title"] = (candidate_title or seg.get("title") or f"Section p{seg.get('start_page')}").strip()[:120]

        # Clean trivial artifacts in title (pipes, column headers)
        seg["title"] = re.sub(r'^\|+\s*', '', seg["title"]).strip()
        seg["title"] = seg["title"].replace("  ", " ").strip()

        # If chunk text is extremely long, optionally split into word-bound chunks (later)
        out.append(seg)

    # Remove consumed markers and empties
    processed = []
    for s in out:
        if s.get("_consumed"):
            continue
        # Clean text: remove repeated "CONFIDENTIAL" etc and excessive whitespace
        text = s.get("text","")
        text = re.sub(r'CONFIDENTIAL', ' ', text, flags=re.I)
        text = re.sub(r'\s+', ' ', text).strip()
        s["text"] = text
        processed.append(s)
    return processed

def postprocess_and_chunk(groups: Dict[str, List[Dict[str, Any]]], llm_model: Optional[str]=None, out_path: Optional[Path]=None):
    # optionally load llm pipeline for title generation if requested
    llm = None
    if llm_model and HAVE_TRANSFORMERS:
        try:
            # text-generation pipeline is enough for short title generation
            llm = pipeline("text-generation", model=llm_model, device_map="auto", return_full_text=False)
            print("Loaded LLM:", llm_model)
        except Exception as e:
            print("Failed to load LLM pipeline:", e)
            llm = None
    improved = []
    for source_file, group in groups.items():
        # filter out already consumed in previous passes
        # we will operate on a shallow copy list to enable index-based merging
        group_copy = [dict(g) for g in group if not g.get("_consumed")]
        # Stitch and fix titles & tables
        fixed = stitch_tables_and_fix_titles(group_copy, llm=llm)
        # Now assemble final word-sized chunks (merge until TARGET_CHUNK_WORDS)
        buffer = None
        for seg in fixed:
            text = seg.get("text","")
            wcnt = words(text)
            if buffer is None:
                buffer = dict(seg)
                # ensure components
                buffer["_components"] = [{"id": seg.get("id"), "start_page": seg.get("start_page"), "end_page": seg.get("end_page"), "title": seg.get("title")}]
            else:
                # if buffer small, append
                if words(buffer.get("text","")) + wcnt <= TARGET_CHUNK_WORDS or words(buffer.get("text","")) < MIN_WORDS_TO_BE_SELF_CONTAINED:
                    buffer["text"] = (buffer.get("text","") + "\n\n" + text).strip()
                    buffer["end_page"] = max(buffer.get("end_page", seg.get("end_page")), seg.get("end_page"))
                    buffer["_components"].append({"id": seg.get("id"), "start_page": seg.get("start_page"), "end_page": seg.get("end_page"), "title": seg.get("title")})
                else:
                    # flush buffer
                    final_chunk = dict(buffer)
                    final_chunk["id"] = final_chunk.get("id") or str(uuid.uuid4())
                    final_chunk["word_count"] = words(final_chunk.get("text",""))
                    final_chunk["components"] = final_chunk.pop("_components", [])
                    improved.append(final_chunk)
                    # start new buffer with overlap: keep last OVERLAP_WORDS words
                    tail_words = final_chunk.get("text","").split()[-OVERLAP_WORDS:]
                    buffer = dict(seg)
                    buffer["text"] = " ".join(tail_words) + "\n\n" + buffer.get("text","")
                    buffer["_components"] = [{"id": seg.get("id"), "start_page": seg.get("start_page"), "end_page": seg.get("end_page"), "title": seg.get("title")}]
        # flush remaining buffer
        if buffer:
            final_chunk = dict(buffer)
            final_chunk["id"] = final_chunk.get("id") or str(uuid.uuid4())
            final_chunk["word_count"] = words(final_chunk.get("text",""))
            final_chunk["components"] = final_chunk.pop("_components", [])
            improved.append(final_chunk)

    # Final cleaning pass: short chunks merging
    final = []
    i = 0
    while i < len(improved):
        c = improved[i]
        if c.get("word_count",0) < MIN_WORDS_TO_BE_SELF_CONTAINED and i+1 < len(improved):
            # merge small chunk with next
            nxt = improved[i+1]
            merged = dict(c)
            merged["text"] = (c.get("text","") + "\n\n" + nxt.get("text","")).strip()
            merged["end_page"] = max(c.get("end_page",0), nxt.get("end_page",0))
            merged["id"] = str(uuid.uuid4())
            merged["word_count"] = words(merged["text"])
            merged["components"] = c.get("components",[]) + nxt.get("components",[])
            final.append(merged)
            i += 2
        else:
            final.append(c)
            i += 1

    # write output
    if out_path:
        with out_path.open("w", encoding="utf-8") as f:
            for ch in final:
                # compact metadata
                out_obj = {
                    "id": ch.get("id"),
                    "title": ch.get("title") or (ch.get("components",[{}])[0].get("title","") if ch.get("components") else ""),
                    "source_file": ch.get("source_file"),
                    "start_page": ch.get("start_page"),
                    "end_page": ch.get("end_page"),
                    "is_table": bool(ch.get("is_table", False)),
                    "text": ch.get("text"),
                    "word_count": ch.get("word_count"),
                    "components": ch.get("components", [])
                }
                f.write(json.dumps(out_obj, ensure_ascii=False) + "\n")
        print("Wrote improved chunks to", out_path)
    return final

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", required=True, dest="infile", help="input clean_chunks.jsonl")
    ap.add_argument("--out", required=True, dest="outfile", help="output improved jsonl")
    ap.add_argument("--llm_model", default=None, help="optional LLM HF id or path for title generation (transformers pipeline)")
    args = ap.parse_args()

    infile = Path(args.infile)
    outfile = Path(args.outfile)
    chunks = load_chunks(infile)
    print(f"Loaded {len(chunks)} segments from {infile}")
    groups = group_by_pages(chunks)
    improved_chunks = postprocess_and_chunk(groups, llm_model=args.llm_model, out_path=outfile)
    print("Improved chunk count:", len(improved_chunks))

if __name__ == "__main__":
    main()