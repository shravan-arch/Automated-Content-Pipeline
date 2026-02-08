import os
from pypdf import PdfReader
from docx import Document
import google.generativeai as genai

# Configure Gemini using environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-2.5-flash"


def load_text(file_path: str) -> str:
    """Extract text from TXT, PDF, or DOCX."""
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)

    raise ValueError("Unsupported file format")


def chunk_text(text: str, chunk_size: int = 900) -> list[str]:
    """Split text into word-based chunks."""
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]


def summarize_chunk(chunk: str) -> str:
    """Summarize a single chunk using Gemini."""
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(
        f"Summarize the following content clearly and concisely:\n\n{chunk}"
    )
    return response.text.strip()


def summarize_document(file_path: str) -> str:
    """
    Full summarization pipeline.
    """
    text = load_text(file_path)
    chunks = chunk_text(text)

    summaries = []
    for idx, chunk in enumerate(chunks, start=1):
        summaries.append(f"Chunk {idx} Summary:\n{summarize_chunk(chunk)}\n")

    return "\n".join(summaries)
