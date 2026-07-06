from pathlib import Path
from shutil import copyfileobj
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.core.config import ALLOWED_EXTENSIONS, UPLOAD_DIR

from app.services.document_processor import get_document_type
from app.services.pdf_parser_service import extract_text_from_pdf
from app.services.ocr_service import extract_text_from_image
from app.services.text_cleaning_service import clean_extracted_text
from app.services.chunking_service import split_text_into_chunks

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

    # Determine the document type
    document_type = get_document_type(file_path)
    extracted_text = None

    # Extract text based on document type
    if document_type == "pdf":
        extracted_text = extract_text_from_pdf(file_path)
    
    if document_type == "image":
        extracted_text = extract_text_from_image(file_path)

    # Clean the extracted text
    cleaned_text = clean_extracted_text(extracted_text)

    # Split the cleaned text into chunks
    chunks = split_text_into_chunks(cleaned_text)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "document_type": document_type,
        "saved_path": str(file_path),
        "extracted_text_preview": extracted_text[:500] if extracted_text else None,
        "text_length": len(extracted_text) if extracted_text else 0,
        "cleaned_text_length": len(cleaned_text),
        "cleaned_text_preview": cleaned_text[:500] if cleaned_text else None,
        "number_of_chunks": len(chunks),
        "first_chunk_preview": chunks[0][:500] if chunks else None,
        "second_chunk_preview": chunks[1][:500] if len(chunks) > 1 else None,
        "message": "File uploaded successfully.",
  
    }