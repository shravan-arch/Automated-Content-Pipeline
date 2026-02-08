# System Architecture

The Relevance Agent follows a modular pipeline architecture designed for scalability and maintainability.

## Architectural Components

- Input Handling  
  Accepts documents from local storage or external file paths.

- Text Extraction  
  Extracts text from supported formats including TXT, PDF, and DOCX.

- Chunking  
  Divides large documents into smaller, manageable segments to avoid token overflow.

- Importance-Based Summarization  
  Each chunk is analyzed for relevance and summarized accordingly.

- Final Summary Generation  
  Partial summaries are merged to produce a coherent and concise final output.

Document Input
↓
Text Extraction
↓
Chunking Engine
↓
Importance-Based Summarization
↓
Partial Summaries
↓
Final Summary Generation
↓
Output File

This layered architecture ensures efficient processing and easy extensibility.
