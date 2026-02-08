import os
import sys
import time
from docx import Document
from pypdf import PdfReader
from google import genai

MODEL_NAME = "models/gemini-flash-latest"
INPUT_FOLDER = "input"

CHUNK_WORDS = 900          
DELAY_SECONDS = 2          
FINAL_SUMMARY_WORDS = 250 

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def read_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def read_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

def read_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n"
    return text

def load_input_text():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if not os.path.exists(path):
            raise Exception(f"❌ File not found: {path}")
    else:
        if not os.path.exists(INPUT_FOLDER):
            raise Exception("❌ Create an 'input' folder or pass a file path.")
        files = os.listdir(INPUT_FOLDER)
        if not files:
            raise Exception("❌ Input folder is empty.")
        path = os.path.join(INPUT_FOLDER, files[0])

    if path.endswith(".txt"):
        return read_txt(path)
    if path.endswith(".docx"):
        return read_docx(path)
    if path.endswith(".pdf"):
        return read_pdf(path)

    raise Exception("❌ Unsupported file type")

def chunk_text(text, words_per_chunk):
    words = text.split()
    return [
        " ".join(words[i:i + words_per_chunk])
        for i in range(0, len(words), words_per_chunk)
    ]

def summarize_chunk_with_importance(chunk_text):
    prompt = f"""
Analyze the following text chunk.

Step 1: Determine its importance level:
- HIGH: core concepts, definitions, main arguments
- MEDIUM: explanations and elaborations
- LOW: examples, background, repetition

Step 2: Summarize the chunk based on importance:
- HIGH → 120–150 words
- MEDIUM → 60–80 words
- LOW → 30–40 words

Rules:
- Do NOT add new information
- Stay strictly within the given text
- Clearly mention the importance level at the top

TEXT:
{chunk_text}
"""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text

def generate_final_summary(partial_summaries):
    merged = "\n".join(partial_summaries)

    prompt = f"""
Create a coherent final summary from the following importance-based summaries.

Rules:
- Do not add new information
- Preserve emphasis from HIGH-importance sections
- Length: {FINAL_SUMMARY_WORDS} words
- Clear academic structure

SUMMARIES:
{merged}
"""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text

def main():
    print("📄 Loading input...")
    text = load_input_text()

    print("✂️ Chunking document...")
    chunks = chunk_text(text, CHUNK_WORDS)
    print(f"🔹 Total chunks: {len(chunks)}")

    summaries = []

    for i, chunk in enumerate(chunks, 1):
        print(f"🧠 Processing chunk {i}/{len(chunks)}")
        summary = summarize_chunk_with_importance(chunk)
        summaries.append(summary)
        time.sleep(DELAY_SECONDS)

    print("🔗 Generating final summary...")
    final_summary = generate_final_summary(summaries)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(final_summary)

    print("✅ DONE")
    print("📄 Output saved to output.txt")

if __name__ == "__main__":
    main()
