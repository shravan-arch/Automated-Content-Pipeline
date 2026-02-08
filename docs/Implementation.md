# Implementation and Unique Feature

The Relevance Agent is implemented in Python using the Google Gemini API for text generation. Python libraries are used for document parsing and text handling.

## Importance-Based Summarization (Unique Feature)

Unlike traditional summarization systems, this project introduces an adaptive importance-based mechanism.

- Each document chunk is classified as High, Medium, or Low importance
- Summary length is dynamically adjusted based on importance
- Critical concepts receive deeper summaries
- Less relevant sections are compressed

This feature enhances summary relevance without increasing API usage, making the system both efficient and intelligent.
