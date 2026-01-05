# test_load_4bit.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import BitsAndBytesConfig

MODEL_ID = "E:/Meta-Llama-3-8B-Instruct"  # replace with exact HF id or local path

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float16
)

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, use_fast=False)
print("Loading model in 4-bit (this may take a minute)...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    quantization_config=bnb_config,
    device_map="auto",
    torch_dtype=torch.float16
)
print("Model loaded. Device map:", getattr(model, "hf_device_map", None))
prompt = "### Instruction:\nWhat is the part number of SCD Processor?\n\n### Response:\n"
inputs = tokenizer(prompt, return_tensors="pt").to(next(model.parameters()).device)
out = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(out[0], skip_special_tokens=True))