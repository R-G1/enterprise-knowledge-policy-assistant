from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_document(file_path: Path):
    text = file_path.read_text(encoding="utf-8")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    documents = []

    for chunk in chunks:
        document = Document(
            page_content=chunk,
            metadata={
                "source": file_path.name,
                "document_type": "policy"
            }
        )

        documents.append(document)

    return documents


if __name__ == "__main__":
    file_path = Path("data/documents/leave_policy.txt")

    documents = chunk_document(file_path)

    print(f"Number of chunks: {len(documents)}")

    for index, document in enumerate(documents, start=1):
        print(f"\n--- Chunk {index} ---")
        print(document.page_content)
        print(f"Metadata: {document.metadata}")