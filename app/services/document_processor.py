from pathlib import Path

from fastapi import HTTPException

from app.core.config import ALLOWED_EXTENSIONS


def get_document_type(file_path: Path) -> str:
    file_extension = file_path.suffix.lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Only PDF, JPG, JPEG, and PNG files are allowed.",
        )

    if file_extension == ".pdf":
        return "pdf"

    if file_extension in {".jpg", ".jpeg", ".png"}:
        return "image"

    raise HTTPException(
        status_code=400,
        detail="Unsupported document type.",
    )