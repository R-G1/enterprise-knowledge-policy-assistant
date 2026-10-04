from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Paths
DOCUMENTS_PATH = Path("data/documents")
CHROMA_PATH = "chroma_db"

# Embedding model
MODEL_NAME = "all-MiniLM-L6-v2"

# Load embedding model
embedding_model = SentenceTransformer(MODEL_NAME)

# Create ChromaDB client
client = chromadb.PersistentClient(path=CHROMA_PATH)

# Create or get collection
collection = client.get_or_create_collection(
    name="enterprise_policies"
)


def load_and_chunk_documents():
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = []

    for file_path in DOCUMENTS_PATH.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        chunks = splitter.split_text(text)

        for chunk in chunks:
            documents.append(
                {
                    "text": chunk,
                    "source": file_path.name,
                    "document_type": "policy"
                }
            )

    return documents


def store_documents():
    documents = load_and_chunk_documents()

    texts = [document["text"] for document in documents]

    embeddings = embedding_model.encode(texts).tolist()

    ids = [
        f"chunk_{index}"
        for index in range(len(documents))
    ]

    metadatas = [
        {
            "source": document["source"],
            "document_type": document["document_type"]
        }
        for document in documents
    ]

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(documents)} chunks in ChromaDB.")


if __name__ == "__main__":
    store_documents()