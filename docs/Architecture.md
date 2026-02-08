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

# System Interaction Diagram

## Client–Edge–AI Communication Flow

```mermaid
sequenceDiagram
    autonumber

    participant B as Browser<br/>(React SPA)
    participant E as Edge Function<br/>(/functions/v1/chat)
    participant G as AI Gateway<br/>(Gemini 3 Flash)

    %% Client to Edge
    B->>E: POST /chat
    activate E

    %% Edge to AI Gateway
    E->>G: POST /v1/chat/completions
    activate G

    %% AI streaming response
    G-->>E: HTTPS Response (Streamed Tokens)
    deactivate G

    %% SSE stream back to browser
    E-->>B: SSE Stream (Real-time tokens)
    deactivate E

This layered architecture ensures efficient processing and easy extensibility.


