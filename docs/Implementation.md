# Implementation Details

## Backend Implementation

The backend is implemented in Python and includes:
- Text extraction using `pypdf` and `python-docx`
- Word-based chunking for large documents
- Chunk-wise summarization using the Gemini API
- Aggregation of partial summaries into a final coherent output

## Frontend Implementation

The optional Streamlit frontend allows users to:
- Upload documents through a browser
- Trigger summarization interactively
- View and download generated summaries

Both CLI and frontend interfaces invoke the same backend function, ensuring consistency and avoiding code duplication.
