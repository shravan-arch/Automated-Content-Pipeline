# Working Flow and Data Flow

## Working Flow

### CLI Mode
1. User runs the script via terminal
2. File path is validated
3. Text is extracted
4. Text is split into chunks
5. Each chunk is summarized
6. Partial summaries are merged
7. Final output is saved

### Web UI Mode
1. User uploads document via Streamlit
2. File is stored locally
3. Backend pipeline is executed
4. Summary is displayed and downloadable

## Data Flow Diagram (DFD)

### Level-0
- User provides document
- System returns summarized output

### Level-1
- Document Input Handler
- Text Extraction Module
- Chunking Module
- Summarization Module
- Output Generator
