from pathlib import Path


try:
    import PyPDF2

    def extract_pdf(path):
        text = ""
        with open(path, "rb") as file_handle:
            reader = PyPDF2.PdfReader(file_handle)
            for page in reader.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
        return text
except ImportError:
    try:
        import fitz

        def extract_pdf(path):
            text = ""
            with fitz.open(path) as document:
                for page in document:
                    text += page.get_text() + "\n"
            return text
    except ImportError:

        def extract_pdf(path):
            return "Could not import PyPDF2 or fitz"


BASE_DIR = Path(__file__).resolve().parent


def load_documents():
    docs = {}

    for file_path in BASE_DIR.rglob("*.pdf"):
        docs[str(file_path.relative_to(BASE_DIR))] = extract_pdf(file_path)

    for file_path in BASE_DIR.rglob("*.md"):
        if file_path.name == Path(__file__).name:
            continue
        with open(file_path, "r", encoding="utf-8") as file_handle:
            docs[str(file_path.relative_to(BASE_DIR))] = file_handle.read()

    return docs


def print_summary(docs):
    for file_name, content in docs.items():
        print(f"--- FILE: {file_name} (length: {len(content)}) ---")
        preview = content[:1000]
        if len(content) > 1000:
            preview += "..."
        print(preview)
        print()


def print_document_inventory():
    print(f"--- Files in {BASE_DIR} ---")
    for file_path in sorted(BASE_DIR.rglob("*.pdf")):
        print(str(file_path.relative_to(BASE_DIR)))
    for file_path in sorted(BASE_DIR.rglob("*.md")):
        if file_path.name == Path(__file__).name:
            continue
        print(str(file_path.relative_to(BASE_DIR)))


def main():
    docs = load_documents()
    print_summary(docs)
    print_document_inventory()


if __name__ == "__main__":
    main()