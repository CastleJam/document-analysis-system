from pathlib import Path

import pytesseract
from PIL import Image


def extract_text_from_image(file_path: Path) -> str:
    image = Image.open(file_path)

    extracted_text = pytesseract.image_to_string(
        image,
        lang="tur+eng",
    )

    return extracted_text.strip()