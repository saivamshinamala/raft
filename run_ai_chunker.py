from transformers import pipeline
from pdf_ai_chunker import run_pdf_to_chunks

llm = pipeline("text-generation",
               model="E:/Meta-Llama-3-8B-Instruct",
               device_map="auto",
               return_full_text=False)

run_pdf_to_chunks("data/pdf/Shakti Userhand Book for Bot.pdf", llm, "data/ai_pdf_chunks/clean_chunks.jsonl")