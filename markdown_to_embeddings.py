#!/usr/bin/env python3
import json
import os
import re
import torch
from sentence_transformers import SentenceTransformer
import nltk

# Ensure NLTK data is present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.tokenize import sent_tokenize

# ----------------- Configure paths here -----------------
INPUT_MD = r"Shakti Userhand Book for Bot.md"
OUTPUT_JSONL = r"output.jsonl"
MODEL_PATH = r"D:\Machine Learning and LLMs\LLMs\all-MiniLM-L6-v2"
# -------------------------------------------------------

CHUNK_MAX_CHARS = 1200
OVERLAP_CHARS = 200
BATCH_SIZE = 64
USE_FP16 = True 

try:
    from tqdm.auto import tqdm
except ImportError:
    class tqdm:
        def __init__(self, total=0, desc=""): self.total, self.n, self.desc = total, 0, desc
        def update(self, n=1): self.n += n; print(f"{self.desc}: {self.n}/{self.total}", end='\r')
        def close(self): print()

HEADING_RE = re.compile(r'^(#{1,6})\s*(.+)$', re.MULTILINE)

def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def split_into_sections(md_text):
    """Generator to yield sections one by one to save memory."""
    matches = list(HEADING_RE.finditer(md_text))
    if not matches:
        yield {"headings": [], "content": md_text}
        return

    heading_stack = []
    for i, m in enumerate(matches):
        level = len(m.group(1))
        title = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        content = md_text[start:end].strip()

        while heading_stack and heading_stack[-1][0] >= level:
            heading_stack.pop()
        heading_stack.append((level, title))
        yield {"headings": [t for _, t in heading_stack], "content": content}

def chunk_text_sentencewise(text):
    """Chunks text into segments of CHUNK_MAX_CHARS using sentence boundaries."""
    sents = sent_tokenize(text)
    if not sents: return []
    
    chunks = []
    current_chunk_sents = []
    current_length = 0
    
    for sentence in sents:
        sent_len = len(sentence)
        # If adding this sentence exceeds limit, save current chunk
        if current_length + sent_len > CHUNK_MAX_CHARS and current_chunk_sents:
            chunks.append(" ".join(current_chunk_sents))
            # Start new chunk with overlap (keep the last sentence of previous chunk)
            overlap_sent = current_chunk_sents[-1] if len(current_chunk_sents) > 0 else ""
            current_chunk_sents = [overlap_sent, sentence] if overlap_sent else [sentence]
            current_length = len(" ".join(current_chunk_sents))
        else:
            current_chunk_sents.append(sentence)
            current_length += sent_len + 1 # +1 for the space
            
    if current_chunk_sents:
        chunks.append(" ".join(current_chunk_sents))
        
    return chunks

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Torch CUDA available: {torch.cuda.is_available()}; using device = {device}")

    if not os.path.exists(INPUT_MD):
        print(f"Error: File '{INPUT_MD}' not found.")
        return

    # Load Model
    print(f"Loading model from {MODEL_PATH}...")
    model = SentenceTransformer(MODEL_PATH, device=device)
    if USE_FP16 and device == "cuda":
        model.half()

    # Read file
    with open(INPUT_MD, 'r', encoding='utf-8') as f:
        md_text = f.read()

    src_basename = os.path.splitext(os.path.basename(INPUT_MD))[0]
    sections = list(split_into_sections(md_text))
    
    print(f"Split file into {len(sections)} sections. Starting embedding...")

    with open(OUTPUT_JSONL, "w", encoding="utf-8") as out:
        pbar = tqdm(total=len(sections), desc="Processing Sections")
        total_chunks = 0
        
        for i, sec in enumerate(sections):
            content = normalize_whitespace(sec['content'])
            if not content:
                pbar.update(1)
                continue
            
            # Combine headers and content for better RAG context
            full_text = f"{' > '.join(sec['headings'])}\n{content}"
            text_chunks = chunk_text_sentencewise(full_text)
            
            if text_chunks:
                # Encode chunks for this specific section
                embs = model.encode(text_chunks, batch_size=BATCH_SIZE, show_progress_bar=False)
                
                for ci, (txt, emb) in enumerate(zip(text_chunks, embs)):
                    record = {
                        "id": f"{src_basename}#sec{i}#c{ci}",
                        "text": txt,
                        "metadata": {
                            "source": src_basename,
                            "headings": sec['headings'],
                            "section_idx": i,
                            "chunk_idx": ci
                        },
                        "embedding": emb.tolist()
                    }
                    out.write(json.dumps(record, ensure_ascii=False) + "\n")
                    total_chunks += 1
            
            pbar.update(1)
            
        pbar.close()

    print(f"Success! Processed {len(sections)} sections into {total_chunks} chunks.")
    print(f"Output saved to: {OUTPUT_JSONL}")

if __name__ == "__main__":
    main()