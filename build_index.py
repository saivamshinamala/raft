#!/usr/bin/env python3
"""
Build embeddings and FAISS index from chunks.jsonl.

- Uses sentence-transformers to create embeddings.
- Normalizes embeddings (L2) and uses IndexFlatIP (cosine-like with normalized vectors).
- Saves index (.faiss) and metadata (chunks_meta.pkl) which maps index id -> chunk metadata.
"""
import argparse
import faiss
import os
import json
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

def load_chunks(jsonl_path):
    chunks = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            chunks.append(json.loads(line))
    return chunks

def build(index_out, meta_out, chunks_jsonl, embedding_model_name="D:/Machine Learning and LLMs/LLMs/F2LLM-1.7B", batch_size=64, use_hnsw=False):
    chunks = load_chunks(chunks_jsonl)
    texts = [c["text"] for c in chunks]
    model = SentenceTransformer(embedding_model_name)
    model.max_seq_length = 512

    # embed in batches
    embeddings = []
    for i in tqdm(range(0, len(texts), batch_size), desc="Embedding"):
        batch = texts[i:i+batch_size]
        emb = model.encode(batch, convert_to_numpy=True, show_progress_bar=False)
        embeddings.append(emb)
    if embeddings:
        embeddings = np.vstack(embeddings)
    else:
        embeddings = np.zeros((0, model.get_sentence_embedding_dimension()), dtype=np.float32)

    # L2-normalize for cosine similarity with IndexFlatIP
    faiss.normalize_L2(embeddings)

    d = embeddings.shape[1]
    if use_hnsw:
        # HNSW index for faster queries
        index = faiss.IndexHNSWFlat(d, 64)  # M=64
        index.hnsw.efConstruction = 200
    else:
        index = faiss.IndexFlatIP(d)

    index.add(embeddings.astype(np.float32))
    faiss.write_index(index, index_out)

    # Save metadata aligned to FAISS row order
    with open(meta_out, "wb") as f:
        pickle.dump(chunks, f)

    print(f"Wrote index: {index_out} ({index.ntotal} vectors)")
    print(f"Wrote metadata: {meta_out} ({len(chunks)} entries)")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--chunks", required=True, help="chunks.jsonl")
    p.add_argument("--index_out", default="data/vector_store/faiss.index")
    p.add_argument("--meta_out", default="data/vector_store/chunks_meta.pkl")
    p.add_argument("--embedding_model", default="D:/Machine Learning and LLMs/LLMs/F2LLM-1.7B")
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--use_hnsw", action="store_true")
    args = p.parse_args()
    os.makedirs(os.path.dirname(args.index_out) or ".", exist_ok=True)
    build(args.index_out, args.meta_out, args.chunks, args.embedding_model, args.batch_size, args.use_hnsw)

if __name__ == "__main__":
    main()