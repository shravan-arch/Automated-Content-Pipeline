# System Architecture

The Relevance Agent follows a layered and modular architecture designed to ensure scalability, maintainability, and separation of concerns.

## Architectural Layers

- **User Layer**
  - Command-line user
  - Optional Streamlit web interface user

- **Presentation Layer**
  - Streamlit frontend (optional)
  - Handles file upload and output visualization

- **Application Layer**
  - Python scripts coordinating execution
  - Entry points for CLI and web interface

- **Core Processing Layer**
  - Text extraction
  - Chunking engine
  - Summarization logic

- **AI Integration Layer**
  - Google Gemini API for content generation

This architecture allows multiple interaction modes while maintaining a single, shared backend pipeline.
