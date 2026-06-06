"""
Convert proposal.md -> proposal.pdf using fpdf2's built-in HTML renderer.
Font: uses the system's default core font (Helvetica) which handles ASCII well,
and falls back to multi_cell for paragraph rendering.
"""
import re
from pathlib import Path
from fpdf import FPDF
import markdown as md_lib

BASE = Path(__file__).parent
md_path = BASE / "proposal.md"
pdf_path = BASE / "proposal.pdf"

md_text = md_path.read_text(encoding="utf-8")

# Convert markdown to HTML using the Python markdown library
html_body = md_lib.markdown(
    md_text,
    extensions=["tables", "fenced_code"]
)

html_full = f"""<h1></h1>
{html_body}
"""

pdf = FPDF()
pdf.add_page()
pdf.set_margins(left=20, top=20, right=20)
pdf.set_auto_page_break(auto=True, margin=20)

# fpdf2's write_html handles h1-h6, p, ul/ol, table, strong, em, code
pdf.write_html(html_full)

pdf.output(str(pdf_path))
print(f"PDF created: {pdf_path}")
