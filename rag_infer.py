#!/usr/bin/env python3
"""
RAG inference with extractive-first strategy.
- Do sentence-level retrieval inside the top-k chunks (safer, extractive).
- If a good sentence match exists, return that exact sentence + citation.
- Otherwise fall back to LLM generation with a strict prompt and a final grounding check.

Usage:
  python rag_infer.py --question "What is Shakti EW System?"
  python rag_infer.py --eval data/QAPairs/qa_pairs.jsonl --top_k 5
"""
import argparse
import faiss
import pickle
import json
import os
import time
import re
from typing import List, Dict, Any, Tuple

import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from sentence_transformers import SentenceTransformer, util

# ---------- CONFIG (edit if needed) ----------
MODEL_ID = "E:/Meta-Llama-3-8B-Instruct"
EMBEDDING_MODEL = "D:/Machine Learning and LLMs/LLMs/F2LLM-1.7B"
INDEX_PATH = "data/vector_store/faiss.index"
CHUNKS_META_PATH = "data/vector_store/chunks_meta.pkl"
# ---------------------------------------------

# BitsAndBytes 4-bit config
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float16
)

# Generation defaults (kept conservative)
GENERATION_KWARGS = dict(
    do_sample=False,
    max_new_tokens=256,
)

# Retrieval / grounding thresholds
TOP_K = 6
MAX_CONTEXT_TOKENS = 3000
SENTENCE_SIM_THRESHOLD = 0.58   # tune: 0.55-0.65 range; higher -> fewer extractive returns
CHUNK_SIM_THRESHOLD = 0.28
# ------------------------------------------------------------------

def load_model_tokenizer(model_id=MODEL_ID):
    print("[INFO] Loading tokenizer and 4-bit model...")
    tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=False)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto",
        torch_dtype=torch.float16
    )
    # set eos/pad token to avoid generation warnings
    if tokenizer.eos_token_id is not None:
        GENERATION_KWARGS['eos_token_id'] = tokenizer.eos_token_id
        GENERATION_KWARGS['pad_token_id'] = tokenizer.eos_token_id
    print("[INFO] Model loaded. Device map:", getattr(model, "hf_device_map", None))
    return model, tokenizer

def load_faiss_and_chunks(index_path=INDEX_PATH, chunks_meta_path=CHUNKS_META_PATH):
    if not os.path.exists(index_path):
        raise FileNotFoundError(index_path)
    if not os.path.exists(chunks_meta_path):
        raise FileNotFoundError(chunks_meta_path)
    print("[INFO] Loading FAISS index:", index_path)
    index = faiss.read_index(index_path)
    print("[INFO] Loading chunks metadata:", chunks_meta_path)
    with open(chunks_meta_path, "rb") as f:
        chunks_meta = pickle.load(f)
    print(f"[INFO] index.ntotal={index.ntotal}, loaded {len(chunks_meta)} chunk entries")
    return index, chunks_meta

def init_embedding_model(path=EMBEDDING_MODEL):
    print("[INFO] Loading embedding model:", path)
    emb = SentenceTransformer(path)
    return emb

def retrieve_chunks(query: str, index, chunks_meta, emb_model, top_k=TOP_K):
    q_emb = emb_model.encode([query], convert_to_numpy=True).astype(np.float32)
    if index.ntotal == 0:
        return []
    distances, indices = index.search(q_emb, top_k)
    results = []
    for d, i in zip(distances[0], indices[0]):
        if i < 0 or i >= len(chunks_meta):
            continue
        meta = chunks_meta[i] if isinstance(chunks_meta[i], dict) else {"text": chunks_meta[i]}
        text = meta.get("text", meta.get("chunk", "")) if isinstance(meta, dict) else str(meta)
        results.append({
            "index": int(i),
            "distance": float(d),
            "chunk": text,
            "meta": meta
        })
    return results

_SENT_SPLIT_RE = re.compile(r'(?<=[\.\?\!])\s+')

def split_sentences(text: str) -> List[str]:
    # Lightweight sentence splitter; keeps short sentences intact
    sents = [s.strip() for s in re.split(_SENT_SPLIT_RE, text) if s.strip()]
    # further split very long lines naively if needed
    out = []
    for s in sents:
        if len(s) > 800:
            # break longer content into ~200-300 token chunks by punctuation
            parts = re.split(r'[,;:\n]', s)
            parts = [p.strip() for p in parts if p.strip()]
            out.extend(parts)
        else:
            out.append(s)
    return out

def sentence_level_retrieval(question: str, retrieved_chunks: List[Dict[str, Any]], emb_model, top_n_sentences=5) -> Tuple[Any, float]:
    """
    Return (best_sentence_dict, sim) or (None, 0.0).
    best_sentence_dict = {"sentence": s, "source": src, "page_info": ..., "chunk_index": idx}
    """
    q_emb = emb_model.encode([question], convert_to_numpy=True)
    best = None
    best_sim = -1.0
    # For speed, gather candidate sentences from retrieved chunks
    for r in retrieved_chunks:
        chunk_text = r["chunk"]
        sents = split_sentences(chunk_text)
        if not sents:
            continue
        sent_embs = emb_model.encode(sents, convert_to_numpy=True)
        sims = util.cos_sim(q_emb, sent_embs).numpy()[0]  # shape (n_sents,)
        max_idx = int(np.argmax(sims))
        sim = float(sims[max_idx])
        if sim > best_sim:
            best_sim = sim
            best = {
                "sentence": sents[max_idx],
                "source": r["meta"].get("source_file", r["meta"].get("source", "unknown")),
                "page": r["meta"].get("start_page", r["meta"].get("page", None)),
                "chunk_index": r["index"]
            }
    return (best, best_sim)

def build_context_text(retrieved_chunks: List[Dict[str, Any]], tokenizer, max_tokens=MAX_CONTEXT_TOKENS):
    parts = []
    total_tokens = 0
    for r in retrieved_chunks:
        meta = r["meta"]
        src = meta.get("source_file", meta.get("source", "source"))
        start = meta.get("start_page", "")
        end = meta.get("end_page", "")
        label = f"[Source: {src} pages {start}-{end}]"
        candidate = f"{label}\n{r['chunk']}\n"
        toks = tokenizer(candidate, return_tensors="pt", truncation=False)["input_ids"].shape[1]
        if total_tokens + toks > max_tokens:
            continue
        parts.append(candidate)
        total_tokens += toks
    return "\n\n".join(parts)

PROMPT_STRICT = """You are a precise assistant that MUST use ONLY the CONTEXT below.
Rules:
1) Do NOT invent, infer, or add anything beyond the CONTEXT.
2) If the CONTEXT contains a concise sentence that answers the QUESTION, return that sentence verbatim and include the citation in square brackets.
3) If the CONTEXT does not contain an explicit answer, reply exactly: "I don't have information on that."
4) Keep answers short.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

def generate_answer_llm(model, tokenizer, prompt: str):
    input_ids = tokenizer(prompt, return_tensors="pt").to(next(model.parameters()).device)
    with torch.no_grad():
        out = model.generate(**input_ids, **GENERATION_KWARGS)
    text = tokenizer.decode(out[0], skip_special_tokens=True)
    # strip prompt prefix if returned
    if "ANSWER" in prompt:
        # attempt to keep only generated answer portion
        if "ANSWER" in text:
            text = text.split("ANSWER")[-1].strip(": \n")
    return text.strip()

def is_answer_grounded(answer: str, retrieved_chunks: List[Dict[str, Any]], emb_model, threshold=CHUNK_SIM_THRESHOLD):
    if not answer or answer.strip() == "":
        return False, 0.0
    a_emb = emb_model.encode([answer], convert_to_numpy=True)
    max_sim = 0.0
    for r in retrieved_chunks:
        c_emb = emb_model.encode([r["chunk"]], convert_to_numpy=True)
        sim = float(util.cos_sim(a_emb, c_emb).item())
        if sim > max_sim:
            max_sim = sim
    return (max_sim >= threshold), max_sim

def answer_question(question: str, model, tokenizer, index, chunks_meta, emb_model, top_k=TOP_K):
    retrieved = retrieve_chunks(question, index, chunks_meta, emb_model, top_k=top_k)
    if not retrieved:
        return {"answer": "I don't have information on that.", "sources": [], "method": "none"}

    # 1) Extractive sentence-level retrieval (preferred)
    best_sent, sent_sim = sentence_level_retrieval(question, retrieved, emb_model)
    if best_sent and sent_sim >= SENTENCE_SIM_THRESHOLD:
        ans_text = best_sent["sentence"].strip()
        src = best_sent["source"]
        page = best_sent.get("page")
        citation = f"{src}" + (f" p.{page}" if page else "")
        return {"answer": ans_text, "sources": [citation], "method": "extractive", "similarity": sent_sim}

    # 2) Fallback: let LLM generate using strict prompt (but we will verify grounding)
    context_text = build_context_text(retrieved, tokenizer, max_tokens=MAX_CONTEXT_TOKENS)
    prompt = PROMPT_STRICT.format(context=context_text, question=question)
    llm_answer = generate_answer_llm(model, tokenizer, prompt)
    grounded, sim = is_answer_grounded(llm_answer, retrieved, emb_model)
    if not grounded:
        return {"answer": "I don't have information on that.", "sources": [], "method": "llm_refused", "grounding_sim": sim}
    # collect cited sources (unique)
    sources = []
    for r in retrieved:
        src = r["meta"].get("source_file", r["meta"].get("source", "source"))
        if src not in sources:
            sources.append(src)
    return {"answer": llm_answer, "sources": sources, "method": "llm", "grounding_sim": sim}

def eval_on_qa_pairs(qa_path: str, model, tokenizer, index, chunks_meta, emb_model, top_k=TOP_K):
    print("[EVAL] Loading QA pairs from:", qa_path)
    total = 0
    matched = 0
    with open(qa_path, "r", encoding="utf-8") as f:
        for line in f:
            total += 1
            j = json.loads(line)
            q = j.get("question", "")
            expected = j.get("answer", "")
            res = answer_question(q, model, tokenizer, index, chunks_meta, emb_model, top_k=top_k)
            ok = expected.strip().lower() in res["answer"].strip().lower()
            if ok:
                matched += 1
            print(f"[{total}] Q: {q}\n -> A: {res['answer']}\n   method={res.get('method')} sim={res.get('similarity', res.get('grounding_sim'))} match={ok}\n")
    print(f"[EVAL] {matched}/{total} matched (naive containment).")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", type=str)
    parser.add_argument("--eval", type=str)
    parser.add_argument("--top_k", type=int, default=TOP_K)
    args = parser.parse_args()

    model, tokenizer = load_model_tokenizer()
    index, chunks_meta = load_faiss_and_chunks()
    emb_model = init_embedding_model()

    if args.question:
        start = time.time()
        out = answer_question(args.question, model, tokenizer, index, chunks_meta, emb_model, top_k=args.top_k)
        print("\n=== ANSWER ===")
        print(out["answer"])
        print("Sources:", out.get("sources"))
        print("Method:", out.get("method"))
        print("Sim:", out.get("similarity", out.get("grounding_sim")))
        print("Time:", time.time() - start)
    elif args.eval:
        eval_on_qa_pairs(args.eval, model, tokenizer, index, chunks_meta, emb_model, top_k=args.top_k)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()