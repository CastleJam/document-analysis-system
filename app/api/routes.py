from pathlib import Path
from shutil import copyfileobj
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.core.config import ALLOWED_EXTENSIONS, UPLOAD_DIR

from app.services.document_processor import get_document_type

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Document Analysis System is running."
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@router.post("/upload")
def upload_document(file: UploadFile = File(...)):
    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Only PDF, JPG, JPEG, and PNG files are allowed.",
        )

    

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        copyfileobj(file.file, buffer)

    document_type = get_document_type(file_path)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "document_type": document_type,
        "saved_path": str(file_path),
        "message": "File uploaded successfully.",
  
    }