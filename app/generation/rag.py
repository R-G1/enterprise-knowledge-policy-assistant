from langchain_ollama import ChatOllama

from app.retrieval.search import search_documents


llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


def generate_answer(query: str):
    # Retrieve relevant document chunks
    results = search_documents(query, top_k=3)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    # Combine retrieved chunks into context
    context_parts = []

    for document, metadata in zip(documents, metadatas):
        context_parts.append(
            f"Source: {metadata['source']}\n"
            f"Content: {document}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are an Enterprise Knowledge and Policy Assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, say:
"I could not find this information in the available company policies."

Do not make up information.

Context:
{context}

User Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content, metadatas


if __name__ == "__main__":
    query = "How many annual leave days can I carry forward?"

    answer, metadatas = generate_answer(query)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    sources = set()

    for metadata in metadatas:
        sources.add(metadata["source"])

    for source in sources:
        print(f"- {source}")