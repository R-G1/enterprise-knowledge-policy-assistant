from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def generate_embedding(text: str):
    embedding = model.encode(text)

    return embedding


if __name__ == "__main__":
    text = "Employees are entitled to 24 days of annual leave."

    embedding = generate_embedding(text)

    print(f"Embedding dimensions: {len(embedding)}")
    print(f"First 5 values: {embedding[:5]}")