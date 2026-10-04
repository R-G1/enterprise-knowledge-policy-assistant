from pathlib import Path

from app.ingestion.chunker import chunk_text


def test_chunking():
    documents_path = Path("data/documents")

    for file_path in documents_path.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        print(f"\nLoaded: {file_path.name}")
        print(f"Original characters: {len(text)}")

        chunks = chunk_text(text)

        print(f"Number of chunks: {len(chunks)}")

        for i, chunk in enumerate(chunks, start=1):
            print(f"\n----- CHUNK {i} -----")
            print(f"Characters: {len(chunk)}")
            print(chunk)

            print("-" * 40)


if __name__ == "__main__":
    test_chunking()