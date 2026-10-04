import chromadb
from sentence_transformers import SentenceTransformer


CHROMA_PATH = "chroma_db"
MODEL_NAME = "all-MiniLM-L6-v2"

# Load embedding model
embedding_model = SentenceTransformer(MODEL_NAME)

# Connect to existing ChromaDB
client = chromadb.PersistentClient(path=CHROMA_PATH)

# Get our existing collection
collection = client.get_collection(
    name="enterprise_policies"
)


def search_documents(query: str, top_k: int = 3):
    # Convert the user query into an embedding
    query_embedding = embedding_model.encode(query).tolist()

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


if __name__ == "__main__":
    query = "How many annual leave days can I carry forward?"

    results = search_documents(query)

    print(f"\nQuery: {query}")
    print("\nRelevant chunks:\n")

    for index, document in enumerate(results["documents"][0], start=1):
        metadata = results["metadatas"][0][index - 1]

        print(f"--- Result {index} ---")
        print(document)
        print(f"Source: {metadata['source']}")
        print()