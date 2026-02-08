# Automated Content Pipeline

This Agent is an AI-powered document summarization system designed to efficiently process large textual documents using Google Gemini. The project supports both **command-line (CLI)** execution and an **optional Streamlit-based web interface**, enabling flexible and user-friendly interaction while reusing a single backend summarization engine.

The system is built to handle large documents (10,000+ words) through hierarchical chunk-based processing and quota-safe API usage, making it suitable for academic projects, research assistance, and personal productivity tools.

## Key Features

- Supports large documents (10,000+ words)
- Accepts TXT, PDF, and DOCX formats
- Dual interface support:
  - CLI (command-line execution)
  - Web UI (Streamlit frontend)
- Shared backend summarization engine
- Modular and extensible architecture
- Quota-safe interaction with Gemini API
- Clean academic and production-ready design

## System Overview

The Agent follows a modular pipeline:

1. Document input (local file or upload)
2. Text extraction based on file type
3. Chunking of large documents
4. Chunk-wise summarization using Gemini
5. Merging partial summaries
6. Final summary generation and output

Both CLI and Streamlit interfaces invoke the same backend pipeline, ensuring consistency and avoiding code duplication.

## Installation

### Prerequisites
- Python 3.10 or higher
- Google Gemini API key

### Install Dependencies
pip install -r requirements.txt

## Set API Key (Windows)
setx GEMINI_API_KEY "YOUR_API_KEY"

## Usage
CLI Mode
Run the summarizer from the terminal:
python run.py (path/to/document.pdf)

## Web Interface (Streamlit)
Launch the Streamlit application:
streamlit run app.py

# Documentation
Detailed project documentation is available in the docs/ directory, including:

- Abstract and Introduction
- Objectives and Scope
- System Architecture
- Design Methodology
- Implementation Details
- Working Flow and DFD
- Unique Features
- Limitations and Future Enhancements
