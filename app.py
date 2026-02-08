import streamlit as st
import os
from summarizer import summarize_document

# Page configuration
st.set_page_config(
    page_title="Relevance Agent",
    layout="wide"
)

st.title("📄 Relevance Agent")
st.subheader("AI-powered document summarization")

st.write(
    "Upload a document (TXT, PDF, DOCX) and generate a concise, relevance-aware summary."
)

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["txt", "pdf", "docx"]
)

if uploaded_file is not None:
    os.makedirs("input", exist_ok=True)
    file_path = os.path.join("input", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully.")

    if st.button("Generate Summary"):
        with st.spinner("Summarizing document..."):
            summary = summarize_document(file_path)

        st.subheader("📌 Generated Summary")
        st.text_area(
            "Summary Output",
            summary,
            height=350
        )

        os.makedirs("output", exist_ok=True)
        output_path = "output/summary.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)

        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

        st.success("Summary generated and saved.")
