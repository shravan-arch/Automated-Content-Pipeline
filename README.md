# Automated-Content-Pipeline
AI-powered document summarization system that processes large text documents using importance-based approach. It supports multiple file formats and generates concise, relevant summaries while operating safely within free-tier API limits.

A key highlight of this project is **importance-based summarization**, where critical sections of a document receive more detailed summaries than less important sections. This approach improves relevance and mimics human reading behavior without increasing API usage.


## Key Features

- Supports large documents (10,000+ words)
- Accepts TXT, PDF, and DOCX file formats
- Importance-based adaptive summarization (unique feature)
- Hierarchical chunk-based processing
- Quota-safe and free-tier friendly design
- Supports external file paths from local storage


## How It Works

1. The user provides a document from local storage.
2. The system extracts text based on file type.
3. Large documents are divided into smaller chunks.
4. Each chunk is analyzed for importance and summarized accordingly.
5. Partial summaries are merged to generate a final coherent summary.
