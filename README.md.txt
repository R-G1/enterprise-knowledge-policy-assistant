# Enterprise Knowledge and Policy Assistant

A RAG-based enterprise knowledge assistant that allows users to ask questions about company policies and receive answers grounded in internal documents.

## Architecture

User
↓
Streamlit Frontend
↓
FastAPI Backend
↓
RAG Pipeline
↓
ChromaDB Vector Database
↓
Llama 3.2 Local LLM

## Technologies Used

- Python
- LangChain
- Sentence Transformers
- all-MiniLM-L6-v2
- ChromaDB
- FastAPI
- Uvicorn
- Streamlit
- Ollama
- Llama 3.2

## RAG Pipeline

1. Load enterprise policy documents.
2. Split documents into smaller chunks.
3. Add metadata such as source and document type.
4. Generate embeddings using all-MiniLM-L6-v2.
5. Store embeddings and metadata in ChromaDB.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant document chunks.
8. Pass the retrieved context to Llama 3.2.
9. Generate an answer grounded in the retrieved documents.
10. Return the answer along with the source documents.

## Project Structure

```text
Enterprise Knowledge and Policy Assistant/
│
├── app/
│   ├── api/
│   │   └── main.py
│   │
│   ├── generation/
│   │   └── rag.py
│   │
│   ├── ingestion/
│   │   └── chunker.py
│   │
│   ├── retrieval/
│   │   ├── embedding.py
│   │   ├── search.py
│   │   └── vector_store.py
│   │
│   └── frontend.py
│
├── data/
│   └── documents/
│
├── chroma_db/
│
├── .gitignore
├── requirements.txt
└── Readme.md