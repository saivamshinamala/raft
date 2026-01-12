import markdown
from bs4 import BeautifulSoup

def load_markdown(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        return f.read()

def markdown_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text("\n")

def chunk_text(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks
