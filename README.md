# Local AI Agent RAG (Retrieval-Augmented Generation)

A local AI-powered restaurant review question-answering system using LangChain, Ollama, and Chroma vector database.

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system that allows users to ask questions about a pizza restaurant based on customer reviews. The system uses a local LLM (via Ollama) to generate intelligent responses grounded in actual customer feedback.

## Features

- **Local LLM Integration**: Uses Ollama with Llama 3.2 model for local inference
- **Vector Search**: Chroma vector database for semantic search across reviews
- **RAG Pipeline**: Combines retrieval and generation for context-aware answers
- **Interactive CLI**: User-friendly command-line interface for asking questions
- **Review Management**: Process and index restaurant reviews from CSV data

## Project Structure

```
├── main.py                      # Main chat interface with LangChain
├── search_reviews.py            # Review search and JSON export
├── vector.py                    # Vector database setup and retriever
├── realistic_restaurant_reviews.csv  # Restaurant review data
├── search_results.json          # Search results output
├── chroma_langchain_db/         # Chroma vector database
└── requirements.txt             # Python dependencies
```

## Requirements

- Python 3.8+
- Ollama (with Llama 3.2 model installed)
- Dependencies listed in requirements.txt

## Installation

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install and run Ollama**:
   - Download from [ollama.ai](https://ollama.ai)
   - Pull the Llama 3.2 model:
     ```bash
     ollama pull llama3.2
     ```

## Usage

### Option 1: Main Interactive Chat
```bash
python main.py
```
Interactive conversation about the pizza restaurant using context from reviews.

### Option 2: Review Search
```bash
python search_reviews.py
```
Search reviews and export results to JSON format.

## How It Works

1. **Data Loading**: Reviews from CSV are loaded and processed
2. **Vectorization**: Review text is converted to embeddings using Chroma
3. **Retrieval**: User queries are matched against reviews using semantic similarity
4. **Generation**: Retrieved reviews are passed to the Ollama LLM with a prompt
5. **Response**: LLM generates an answer based on the retrieved context

## Dependencies

- **langchain**: Framework for building LLM applications
- **langchain-ollama**: Ollama integration for LangChain
- **langchain-chroma**: Chroma vector store integration
- **pandas**: Data manipulation and CSV handling

## Example Queries

- "What do customers say about the pizza quality?"
- "Are there any complaints about service?"
- "What's the overall sentiment about the restaurant?"

## Notes

- Ensure Ollama is running before starting the application
- The vector database is cached in `chroma_langchain_db/` for faster subsequent runs
- Reviews are indexed once and reused for multiple queries

## License

This project is part of the GenAI BootCamp Projects.
