from pathlib import Path

import pdfplumber


def extract_text_from_pdf(file_path: Path) -> str:
    extracted_text = ""

    with pdfplumber.open(file_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()

            if page_text:
                extracted_text += f"\n\n--- Page {page_number} ---\n"
                extracted_text += page_text

    return extracted_text.strip()