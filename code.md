
import glob
import os

try:
    import PyPDF2
    def extract_pdf(path):
        text = ""
        with open(path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
except ImportError:
    try:
        import fitz
        def extract_pdf(path):
            text = ""
            doc = fitz.open(path)
            for page in doc:
                text += page.get_text() + "\n"
            return text
    except ImportError:
        def extract_pdf(path):
            return "Could not import PyPDF2 or fitz"

docs = {}
for file in glob.glob("*.pdf"):
    docs[file] = extract_pdf(file)

for file in glob.glob("*.md"):
    with open(file, 'r', encoding='utf-8') as f:
        docs[file] = f.read()

# Print summary of extracted texts to the LLM
for k, v in docs.items():
    print(f"--- FILE: {k} (length: {len(v)}) ---")
    print(v[:1000] + ("..." if len(v) > 1000 else ""))
    print("\n")

import os

dirs_to_check = ['.', '/mnt/data', '/content', '/tmp']
for d in dirs_to_check:
    if os.path.exists(d):
        print(f"--- Files in {d} ---")
        for root, dirs, files in os.walk(d):
            for file in files:
                if file.endswith(('.pdf', '.md')):
                    print(os.path.join(root, file))