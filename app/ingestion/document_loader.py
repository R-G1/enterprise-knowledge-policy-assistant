from pathlib import Path


def load_documents():
    documents_path = Path("data/documents")

    for file_path in documents_path.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        print(f"Loaded: {file_path.name}")
        print(f"Characters: {len(text)}")
        print("Preview:")

        preview = "\n".join(text.splitlines()[:5])
        print(preview)

        print("-" * 40)


if __name__ == "__main__":
    load_documents()