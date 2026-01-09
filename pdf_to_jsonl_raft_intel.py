"""
pdf_to_jsonl_raft_intel.py

Intelligent, high-throughput PDF -> RAFT-friendly JSONL pipeline optimized for local Llama3-8B-Instruct on GPU.

Design goals (for ~700 pages):
- Minimize LLM calls (expensive) by using deterministic extraction + regex normalization first.
- Only call the LLM for pages that need semantic reasoning: ambiguous key-values, poor table quality, or when QA pairs are requested.
- Batch LLM calls to amortize tokenizer/model overhead.
- Use few-shot domain examples in prompts (EW domain) to guide normalization and reduce hallucination.
- Validate LLM outputs deterministically (parsers) and re-query low-confidence fields automatically.
- Emit page-level JSONL records suitable for RAFT fine-tuning and RAG indexing:
  - schema includes chunk_id, page_numbers, sections, key_values (raw + normalized + confidence),
    tables (structured + normalized_columns), document_text, summary, important_entities, qa_pairs, meta.

Requirements:
    pip install pdfplumber transformers torch regex

Usage:
    python pdf_to_jsonl_raft_intel.py --pdf "data\pdf\Shakti Userhand Book for Bot.pdf" --out data/pdf_chunks/output_raft.jsonl --model_path E:/Meta-Llama-3-8B-Instruct --device cuda --batch_size 6

Notes:
- Tweak batch_size and max_new_tokens depending on GPU memory.
- This script favors deterministic normalization and conservative model use to avoid hallucination.
- The few-shot examples in the prompt are realistic EW examples to reduce parsing errors.
"""

import argparse
import json
import math
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pdfplumber
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# -----------------------------
# Configurable thresholds
# -----------------------------
TABLE_NUMERIC_RATIO_THRESHOLD = 0.6    # tables with numeric ratio above this are considered 'good'
KV_REGEX_CONFIDENCE = "high"           # regex-detected key-values get 'high' confidence
LLM_CONFIDENCE_LOW = "low"
LLM_CONFIDENCE_MED = "med"
LLM_CONFIDENCE_HIGH = "high"

# -----------------------------
# Utilities: deterministic parsers
# -----------------------------


def parse_number_and_unit(text: str) -> Tuple[Optional[float], Optional[str], Optional[str]]:
    """
    Try to parse numeric values or ranges with units from text.
    Returns (normalized_value or range dict as float/list -> we will store raw parsed string here),
    unit (string) and confidence label.
    - Handles ranges like '0.175 - 40 GHz', '6–40 GHz', '50 KW', '1 KVA', '10%'.
    - Returns normalized_value as:
        - single float for single numeric value (converted to base, if unit conversion applied)
        - dict {"min": val, "max": val} for ranges
    For safety we return strings for non-parseable; caller will interpret.
    """
    s = text.strip()
    # normalize common unicode dashes
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    # common unit patterns we handle and conversions to base where sensible:
    unit_map = {
        "ghz": 1e9,
        "mhz": 1e6,
        "khz": 1e3,
        "hz": 1.0,
        "kw": 1e3,
        "w": 1.0,
        "kva": 1e3,
        "kg": 1.0,
        "mm": 1.0,
        "cm": 10.0,
        "m": 1000.0,
        "nm": 1852e3,  # nautical mile to meters -> be careful; we keep unit if unsure
        "dbm": 1.0,
        "%": 1.0,
    }

    # Look for numeric range
    range_match = re.search(r"(?P<a>\d+(\.\d+)?)(\s*[-–—]\s*)(?P<b>\d+(\.\d+)?)(?:\s*(?P<unit>[A-Za-z%/°]+))?", s, flags=re.I)
    if range_match:
        a = float(range_match.group("a"))
        b = float(range_match.group("b"))
        unit = (range_match.group("unit") or "").lower()
        if unit in unit_map:
            scale = unit_map[unit]
            # convert to base unit numeric values if unit is frequency/power etc.
            return ({"min": a * scale, "max": b * scale}, unit, LLM_CONFIDENCE_HIGH)
        elif unit:
            return ({"min": a, "max": b}, unit, LLM_CONFIDENCE_MED)
        else:
            return ({"min": a, "max": b}, None, LLM_CONFIDENCE_MED)

    # single numeric with optional unit
    single_match = re.search(r"(?P<num>\d+(\.\d+)?)(\s*(?P<unit>[A-Za-z%/°]+))", s, flags=re.I)
    if single_match:
        num = float(single_match.group("num"))
        unit = (single_match.group("unit") or "").lower()
        if unit in unit_map:
            return (num * unit_map[unit], unit, LLM_CONFIDENCE_HIGH)
        else:
            return (num, unit if unit else None, LLM_CONFIDENCE_MED)

    # special patterns like "100%" or "50 kpps"
    perc_match = re.search(r"(?P<num>\d+(\.\d+)?)\s*%", s)
    if perc_match:
        return (float(perc_match.group("num")), "%", LLM_CONFIDENCE_HIGH)

    # fallback: cannot parse numeric; return raw string and low confidence
    return (None, None, LLM_CONFIDENCE_LOW)


def normalize_part_no(s: str) -> str:
    """Heuristic normalization of part numbers: strip spaces, keep alphanumerics and hyphens."""
    return re.sub(r"[^A-Za-z0-9\-_./]", "", s)


# -----------------------------
# PDF deterministic extraction
# -----------------------------


def group_chars_to_lines(chars: List[Dict[str, Any]], y_tolerance: float = 3.0) -> List[Dict]:
    if not chars:
        return []
    chars = sorted(chars, key=lambda c: (round(c.get("top", 0)), c.get("x0", 0)))
    lines = []
    cur_top = chars[0].get("top", 0)
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
            # heuristic: first row may be header if contains non-numeric tokens
            if non_empty >= 1 and any(any(ch.isalpha() for ch in (cell or "")) for cell in first):
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
# Candidate key-value extraction (deterministic)
# -----------------------------


KV_KEYWORDS = [
    "frequency", "coverage", "df accuracy", "df", "sensitivity", "probability of intercept",
    "power supply", "power", "erp", "frequency coverage", "frequency range", "processing time",
    "mission library", "emitters", "manufacturer", "manufacturer by", "manufactured by", "part no",
    "bel part", "qty", "quantity", "weight", "dimensions", "polarisation", "polarization",
]


def find_candidate_kvs(paragraphs: List[str]) -> List[Dict[str, Any]]:
    """
    Heuristically scan paragraphs for key-like lines and extract key-value candidates using regexes.
    Returns list of {"key": raw_key, "value": raw_value, "source_text": line, "confidence": ...}
    """
    kvs = []
    for p in paragraphs:
        lines = [l.strip() for l in p.split("\n")]
        for ln in lines:
            lln = ln.lower()
            for kw in KV_KEYWORDS:
                if kw in lln:
                    # try to split on colon or hyphen separator
                    if ":" in ln:
                        parts = ln.split(":", 1)
                        key = parts[0].strip()
                        val = parts[1].strip()
                    elif "-" in ln and re.search(r"[A-Za-z]\s*-\s*[A-Za-z]", ln) is None:
                        parts = ln.split("-", 1)
                        key = parts[0].strip()
                        val = parts[1].strip()
                    else:
                        # fallback: use whole line as value and infer key as keyword
                        key = kw
                        val = ln.strip()
                    kvs.append({"key": key, "value": val, "source_text": ln, "confidence": KV_REGEX_CONFIDENCE})
                    break
    return kvs


# -----------------------------
# Table quality heuristics
# -----------------------------


def table_numeric_ratio(table: Dict[str, Any]) -> float:
    """Compute fraction of cells that are numeric-like in a table."""
    rows = table.get("rows", []) or []
    if not rows:
        return 0.0
    total = 0
    numeric = 0
    for r in rows:
        for c in r:
            total += 1
            if c and re.search(r"\d", c):
                numeric += 1
    return numeric / total if total else 0.0


def needs_llm_for_table(table: Dict[str, Any]) -> bool:
    """Decide if table needs LLM semantic normalization."""
    ratio = table_numeric_ratio(table)
    # if few numeric cells OR header ambiguous -> call LLM
    if ratio < TABLE_NUMERIC_RATIO_THRESHOLD:
        return True
    # also call LLM if header names are generic (col_1 etc)
    header = table.get("header") or []
    if any(h and h.lower().startswith("col_") for h in header):
        return True
    return False


# -----------------------------
# LLM prompt building (few-shot + batch)
# -----------------------------


FEW_SHOT_EXAMPLES = [
    # Example 1: Frequency coverage normalization
    {
        "raw": {"page_number": 1, "headings": ["1.1 Introduction"], "paragraphs": ["Frequency Coverage: 0.175 – 40 GHz. The ES system covers..."], "tables": []},
        "out": {
            "key_values": [
                {"key": "frequency_coverage_es", "value": "0.175 – 40 GHz", "normalized_value": {"min_hz": 175000000.0, "max_hz": 40000000000.0}, "unit": "Hz", "confidence": "high"}
            ],
            "summary": "ES frequency coverage is 0.175–40 GHz.",
            "qa_pairs": [{"instruction": "What is the ES frequency coverage?", "response": "0.175 – 40 GHz"}]
        }
    },
    # Example 2: Part numbers and quantities
    {
        "raw": {"page_number": 2, "headings": ["1.3 Equipment List"], "paragraphs": ["Ser 1 | 172300352518 | ES AHU-1 | 1"], "tables": [[["Ser","BEL Part No.","Sub System Description","Qty"], ["1","172300352518","ES AHU-1","1"]]]},
        "out": {
            "key_values": [
                {"key": "bel_part_1", "value": "172300352518", "normalized_value": "172300352518", "unit": None, "confidence": "high"},
                {"key": "qty_1", "value": "1", "normalized_value": 1, "unit": None, "confidence": "high"}
            ],
            "tables": [
                {"header": ["Ser", "BEL Part No.", "Sub System Description", "Qty"], "normalized_columns": {"Ser": "string", "BEL Part No.": "string", "Sub System Description": "string", "Qty": "int"}}
            ],
            "qa_pairs": [{"instruction": "What is the BEL Part No. for item 1?", "response": "172300352518"}]
        }
    },
    # Example 3: Power and ERP
    {
        "raw": {"page_number": 3, "headings": ["EA Segment"], "paragraphs": ["ERP 6-18 GHz 50 KW (average) 18-40 GHz 10 KW"]},
        "out": {
            "key_values": [
                {"key": "erp_6_18_ghz", "value": "50 KW", "normalized_value": 50000.0, "unit": "W", "confidence": "high"},
                {"key": "erp_18_40_ghz", "value": "10 KW", "normalized_value": 10000.0, "unit": "W", "confidence": "high"}
            ],
            "summary": "ERP: 50 kW for 6-18 GHz and 10 kW for 18-40 GHz.",
            "qa_pairs": [{"instruction": "What is the ERP for 6-18 GHz?", "response": "50 KW"}]
        }
    }
]


LLM_PROMPT_TEMPLATE = """
You are an assistant specialized in extracting deterministic facts and structured data from technical PDF pages (naval EW domain).
Given a small list of raw page objects (page_number, headings, paragraphs, tables), output a strict JSON array.
Each page object in output must contain these keys (use exactly these keys at top level):
[
  "page_number", "chunk_id", "source_file", "page_numbers",
  "sections", "key_values", "headings", "paragraphs", "tables",
  "document_text", "summary", "important_entities", "qa_pairs", "meta"
]

Guidelines:
- For key_values: find explicit facts (Frequency Coverage, DF Accuracy, ERP, Part Nos, Qty, Weights, Dimensions, Sensitivity).
  For each key_value include: key (snake_case short id), value (original string), normalized_value (number or dict if range if parseable), unit (if parsed), confidence ("low"|"med"|"high").
- For tables: keep header, rows, structured_rows, and attempt to infer normalized_columns (map header->type).
  Use simple types: "int","float","string","frequency_hz","power_w","weight_kg","dimension_mm","percent","part_no".
- For document_text: combine the most informative heading + first 2 paragraphs + table captions (<= 400 tokens).
- For qa_pairs: produce up to 3 concise instruction->response pairs derived from explicit facts.
- Keep 'summary' to at most 2 sentences.
- Do not hallucinate facts not present in the raw input. If unsure, omit the key_value or set confidence to "low".
- Output only valid JSON (a single JSON array). No extra text.

Few-shot examples (input -> expected behavior):
{examples}

Now process the Raw pages (list of JSON objects):
{raw}
"""

# -----------------------------
# LLM generation helpers
# -----------------------------


def load_model_tokenizer(model_path: str, device: str = "cuda"):
    dtype = torch.float16 if device.startswith("cuda") else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=dtype, trust_remote_code=True)
    if device.startswith("cuda"):
        model = model.to(device)
    model.eval()
    return tokenizer, model


def generate_llm_json(tokenizer, model, batch_raw: List[Dict], source_file: str, device: str,
                      max_new_tokens: int = 512, temperature: float = 0.0) -> str:
    """
    Build prompt with few-shot examples and raw batch; generate and attempt to return the JSON array substring.
    """
    examples_str = []
    for ex in FEW_SHOT_EXAMPLES:
        examples_str.append(json.dumps(ex["raw"], ensure_ascii=False))
    examples_joined = "\n\n".join(examples_str)
    raw_json = json.dumps(batch_raw, ensure_ascii=False, indent=2)
    prompt = LLM_PROMPT_TEMPLATE.format(examples=examples_joined, raw=raw_json)

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
    generation = tokenizer.decode(out_ids[0][input_ids.shape[-1]:], skip_special_tokens=True)
    gen = generation.strip()
    # Extract first JSON array found
    if "[" in gen and "]" in gen:
        start = gen.find("[")
        end = gen.rfind("]") + 1
        return gen[start:end]
    return gen


# -----------------------------
# Post-LLM validation and re-query logic
# -----------------------------


def validate_key_values(kvs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Validate and coerce normalized_values where possible.
    If normalized_value is a dict string, try to parse; if missing, run parse_number_and_unit on raw value.
    """
    validated = []
    for kv in kvs:
        raw_val = kv.get("value", "") or ""
        normalized = kv.get("normalized_value")
        unit = kv.get("unit")
        confidence = kv.get("confidence", LLM_CONFIDENCE_LOW)
        # If model provided normalized_value as numeric/dict, keep but verify types.
        if normalized is None:
            # try deterministic parser
            parsed_val, parsed_unit, parsed_conf = parse_number_and_unit(raw_val)
            if parsed_val is not None:
                kv["normalized_value"] = parsed_val
                kv["unit"] = parsed_unit
                kv["confidence"] = parsed_conf
            else:
                kv["confidence"] = LLM_CONFIDENCE_LOW
        else:
            # keep as is, but if it's a string representing numeric range, try to coerce
            if isinstance(normalized, str):
                pv, pu, pc = parse_number_and_unit(normalized)
                if pv is not None:
                    kv["normalized_value"] = pv
                    kv["unit"] = pu
                    kv["confidence"] = pc
            # else assume model provided a numeric/dict and set med/high confidence if absent
            kv.setdefault("confidence", LLM_CONFIDENCE_MED)
        validated.append(kv)
    return validated


def validate_and_fix_tables(tables: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Deterministically attempt to normalize table columns: detect numeric columns and set normalized_columns.
    """
    out_tables = []
    for t in tables:
        header = t.get("header") or []
        structured_rows = t.get("structured_rows", []) or []
        normalized_columns = {}
        # infer column types by sampling structured_rows
        if structured_rows:
            for col in (header or structured_rows[0].keys()):
                sample_vals = []
                for r in structured_rows[:10]:
                    v = r.get(col, "")
                    sample_vals.append(v)
                # heuristics
                num_count = sum(1 for v in sample_vals if v and re.search(r"\d", str(v)))
                if num_count / max(1, len(sample_vals)) > 0.6:
                    # attempt to see if frequency-like or power-like
                    sample_join = " ".join(map(str, sample_vals)).lower()
                    if "ghz" in sample_join or "mhz" in sample_join:
                        normalized_columns[col] = "frequency_hz"
                    elif "kw" in sample_join or "w" in sample_join:
                        normalized_columns[col] = "power_w"
                    elif re.search(r"\bmm\b|\bcm\b|\bm\b", sample_join):
                        normalized_columns[col] = "dimension_mm"
                    elif re.search(r"\d+\s*kg|\bkg\b", sample_join):
                        normalized_columns[col] = "weight_kg"
                    elif re.search(r"^\d+$", sample_join):
                        normalized_columns[col] = "int"
                    else:
                        normalized_columns[col] = "float"
                else:
                    # mostly non-numeric
                    if any(re.search(r"part|bel|1723|[A-Z]{2,}", str(v)) for v in sample_vals):
                        normalized_columns[col] = "part_no"
                    else:
                        normalized_columns[col] = "string"
        else:
            normalized_columns = {}
        t["normalized_columns"] = normalized_columns
        out_tables.append(t)
    return out_tables


# -----------------------------
# QA pair generation (deterministic fallback)
# -----------------------------


def generate_qa_from_kvs(kvs: List[Dict[str, Any]], max_pairs: int = 3) -> List[Dict[str, str]]:
    pairs = []
    for kv in kvs:
        key = kv.get("key")
        val = kv.get("value")
        if not key or not val:
            continue
        # build a human-friendly question
        q = key.replace("_", " ").capitalize()
        q = f"What is the {q}?"
        pairs.append({"instruction": q, "response": str(val)})
        if len(pairs) >= max_pairs:
            break
    return pairs


# -----------------------------
# High-level pipeline
# -----------------------------


def choose_pages_for_llm(pages_extracted: List[Tuple[int, Dict[str, Any]]]) -> List[int]:
    """
    Decide which page numbers should be sent to LLM based on heuristics:
      - page has any table that requires LLM
      - or candidate_kvs have low-confidence or no candidate_kvs found but page has technical keywords.
    Returns a list of page indices (1-based) that need LLM.
    """
    pages_need = []
    for pn, pe in pages_extracted:
        tables = pe.get("tables", []) or []
        paragraphs = pe.get("paragraphs", []) or []
        # if there is any table that needs semantic typing
        table_flag = any(needs_llm_for_table(t) for t in tables)
        kv_candidates = find_candidate_kvs(paragraphs)
        # if no candidate kvs but page includes many digits/units -> LLM helpful
        tech_density = sum(1 for p in paragraphs for _ in re.finditer(r"\d{2,}", p))
        if table_flag or not kv_candidates and tech_density > 5:
            pages_need.append(pn)
            continue
        # if kvs exist but many are low confidence patterns -> still call LLM to normalize
        low_conf = [k for k in kv_candidates if k.get("confidence") != KV_REGEX_CONFIDENCE]
        if len(low_conf) >= 1 and (len(kv_candidates) < 4 or tech_density > 2):
            pages_need.append(pn)
            continue
    return pages_need


def build_prompt_batch_entries(pages_extracted: List[Tuple[int, Dict[str, Any]]], page_nums: List[int], pdf_name: str,
                               paras_limit: int = 8, table_row_limit: int = 6) -> List[Dict[str, Any]]:
    """
    Build compact raw objects for LLM prompt for the given page_nums (subset).
    """
    entries = []
    lookup = {pn: pe for pn, pe in pages_extracted}
    for pn in page_nums:
        pe = lookup[pn]
        paras = pe.get("paragraphs", [])[:paras_limit]
        tables = []
        for t in pe.get("tables", [])[:6]:
            tables.append({"header": t.get("header"), "rows": t.get("rows", [])[:table_row_limit], "structured_rows": t.get("structured_rows", [])[:table_row_limit]})
        entries.append({"page_number": pn, "headings": pe.get("headings", [])[:6], "paragraphs": paras, "tables": tables, "text_excerpt": (pe.get("raw_text") or "")[:3000], "source_file": pdf_name})
    return entries


def postprocess_llm_page_obj(page_obj: Dict[str, Any], pdf_name: str) -> Dict[str, Any]:
    """
    Ensure schema, validate key_values and tables, generate fallbacks for missing pieces.
    """
    # enforce schema
    pn = page_obj.get("page_number")
    page_obj.setdefault("chunk_id", f"{pdf_name}_page_{pn}")
    page_obj.setdefault("source_file", pdf_name)
    page_obj.setdefault("page_numbers", [pn])
    page_obj.setdefault("sections", page_obj.get("sections", []))
    page_obj.setdefault("headings", page_obj.get("headings", []))
    page_obj.setdefault("paragraphs", page_obj.get("paragraphs", []))
    page_obj.setdefault("tables", page_obj.get("tables", []))
    page_obj.setdefault("document_text", page_obj.get("document_text", "") or "")
    page_obj.setdefault("summary", page_obj.get("summary", "") or "")
    page_obj.setdefault("important_entities", page_obj.get("important_entities", []) or [])
    page_obj.setdefault("qa_pairs", page_obj.get("qa_pairs", []) or [])
    page_obj.setdefault("meta", page_obj.get("meta", {"ocr": False, "confidence": None}))

    # validate key_values
    kvs = page_obj.get("key_values", [])
    page_obj["key_values"] = validate_key_values(kvs)

    # validate tables
    page_obj["tables"] = validate_and_fix_tables(page_obj.get("tables", []))

    # if no qa_pairs, create some from key_values
    if not page_obj.get("qa_pairs"):
        page_obj["qa_pairs"] = generate_qa_from_kvs(page_obj.get("key_values", []), max_pairs=3)

    # conservative trimming of document_text
    if len(page_obj["document_text"]) > 6000:
        page_obj["document_text"] = page_obj["document_text"][:6000]

    return page_obj


def pipeline_process(pdf_path: str, out_path: str, model_path: str, device: str = "cuda",
                     batch_size: int = 6, max_new_tokens: int = 512, paras_limit: int = 8,
                     table_row_limit: int = 6):
    pdf_path = Path(pdf_path)
    out_path = Path(out_path)

    tokenizer, model = load_model_tokenizer(model_path, device=device)

    # Stage 1: Deterministic extraction (fast)
    t0 = time.time()
    pages_extracted = []
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages, start=1):
            pe = extract_page_elements(page)
            pages_extracted.append((i, pe))
            if i % 50 == 0:
                print(f"[extract] {i}/{total} pages extracted")
    t1 = time.time()
    print(f"[extract] Completed deterministic extraction: {len(pages_extracted)} pages in {t1 - t0:.1f}s")

    # Stage 2: Candidate deterministic normalization (fast)
    per_page_candidates = {}
    for pn, pe in pages_extracted:
        kvs = find_candidate_kvs(pe.get("paragraphs", []))
        # run deterministic numeric parser on kvs with low confidence fallback
        validated_kvs = []
        for kv in kvs:
            raw_val = kv.get("value", "")
            parsed, unit, conf = parse_number_and_unit(raw_val)
            if parsed is not None:
                validated_kvs.append({"key": re.sub(r"\s+", "_", kv.get("key", "").lower()), "value": raw_val, "normalized_value": parsed, "unit": unit, "confidence": conf})
            else:
                validated_kvs.append({"key": re.sub(r"\s+", "_", kv.get("key", "").lower()), "value": raw_val, "normalized_value": None, "unit": None, "confidence": kv.get("confidence", "low")})
        per_page_candidates[pn] = {"kvs": validated_kvs, "tables": pe.get("tables", [])}

    # Decide pages that need LLM
    pages_for_llm = choose_pages_for_llm(pages_extracted)
    print(f"[decide] Pages flagged for LLM semantic extraction: {len(pages_for_llm)} pages out of {len(pages_extracted)} total")

    # Stage 3: Batch LLM on flagged pages
    # We'll process pages_for_llm in batches to reduce calls
    llm_batches = [pages_for_llm[i:i + batch_size] for i in range(0, len(pages_for_llm), batch_size)]

    results_by_page = {}  # pn -> final page object

    for bi, batch_page_nums in enumerate(llm_batches, start=1):
        batch_entries = build_prompt_batch_entries(pages_extracted, batch_page_nums, pdf_path.name, paras_limit=paras_limit, table_row_limit=table_row_limit)
        print(f"[llm] Generating batch {bi}/{len(llm_batches)} with {len(batch_entries)} pages ...")
        try:
            generated = generate_llm_json(tokenizer, model, batch_entries, pdf_path.name, device, max_new_tokens=max_new_tokens, temperature=0.0)
            parsed = json.loads(generated)
            if not isinstance(parsed, list):
                raise ValueError("LLM response not a JSON array")
        except Exception as e:
            print(f"[llm] Warning: LLM failed for batch {bi}: {e}. Falling back to deterministic enrichments for these pages.")
            parsed = []
            # deterministic fallback: build page objects with candidate kvs and tables
            for pn in batch_page_nums:
                pe = dict((p, e) for p, e in pages_extracted)[pn]
                page_obj = {
                    "page_number": pn,
                    "chunk_id": f"{pdf_path.name}_page_{pn}",
                    "source_file": pdf_path.name,
                    "page_numbers": [pn],
                    "sections": [],
                    "key_values": per_page_candidates[pn]["kvs"],
                    "headings": pe.get("headings", []),
                    "paragraphs": pe.get("paragraphs", []),
                    "tables": pe.get("tables", []),
                    "document_text": (" ".join(pe.get("headings", [])[:1]) + " " + " ".join(pe.get("paragraphs", [])[:2])).strip(),
                    "summary": "",
                    "important_entities": [],
                    "qa_pairs": generate_qa_from_kvs(per_page_candidates[pn]["kvs"]),
                    "meta": {"ocr": False, "confidence": None},
                }
                parsed.append(page_obj)

        # Postprocess each page object returned from LLM
        for page_obj in parsed:
            pn = page_obj.get("page_number")
            final_obj = postprocess_llm_page_obj(page_obj, pdf_path.name)
            results_by_page[pn] = final_obj
        print(f"[llm] Batch {bi} processed; {len(parsed)} pages parsed.")

    # Stage 4: Assemble final JSONL output (per-page). For pages not sent to LLM, use deterministic candidates.
    with open(out_path, "w", encoding="utf-8") as fout:
        written = 0
        for pn, pe in pages_extracted:
            if pn in results_by_page:
                out_obj = results_by_page[pn]
            else:
                # deterministic page object
                out_obj = {
                    "page_number": pn,
                    "chunk_id": f"{pdf_path.name}_page_{pn}",
                    "source_file": pdf_path.name,
                    "page_numbers": [pn],
                    "sections": [],
                    "key_values": per_page_candidates[pn]["kvs"],
                    "headings": pe.get("headings", []),
                    "paragraphs": pe.get("paragraphs", []),
                    "tables": validate_and_fix_tables(pe.get("tables", [])),
                    "document_text": (" ".join(pe.get("headings", [])[:1]) + " " + " ".join(pe.get("paragraphs", [])[:2])).strip(),
                    "summary": "",
                    "important_entities": [],
                    "qa_pairs": generate_qa_from_kvs(per_page_candidates[pn]["kvs"]),
                    "meta": {"ocr": False, "confidence": None},
                }
            fout.write(json.dumps(out_obj, ensure_ascii=False) + "\n")
            written += 1
            if written % 100 == 0:
                print(f"[write] Wrote {written} pages to output")
    t_end = time.time()
    print(f"[done] Wrote {written} page records to {out_path} in {t_end - t0:.1f}s (total elapsed).")


# -----------------------------
# CLI
# -----------------------------


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Intelligent PDF -> RAFT JSONL pipeline (optimized for local Llama on GPU).")
    parser.add_argument("--pdf", required=True, help="Input PDF file path")
    parser.add_argument("--out", required=True, help="Output JSONL file path")
    parser.add_argument("--model_path", required=True, help="Local Llama3-8B-Instruct model directory")
    parser.add_argument("--device", choices=["cuda", "cpu"], default="cuda", help="Device for model")
    parser.add_argument("--batch_size", type=int, default=6, help="Pages per LLM batch (tune for GPU memory)")
    parser.add_argument("--max_new_tokens", type=int, default=512, help="max_new_tokens for LLM generation")
    parser.add_argument("--paras_limit", type=int, default=8, help="Paragraphs per page included in prompt")
    parser.add_argument("--table_row_limit", type=int, default=6, help="Rows per table included in prompt")
    args = parser.parse_args()

    t_start = time.time()
    pipeline_process(args.pdf, args.out, args.model_path, device=args.device,
                     batch_size=args.batch_size, max_new_tokens=args.max_new_tokens,
                     paras_limit=args.paras_limit, table_row_limit=args.table_row_limit)
    print("Finished total in {:.1f}s".format(time.time() - t_start))