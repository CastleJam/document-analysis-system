from pathlib import Path
from shutil import copyfileobj
from fastapi import APIRouter, File, HTTPException, UploadFile

from app.core.config import ALLOWED_EXTENSIONS, UPLOAD_DIR
from app.core.config import MIN_SIMILARITY_THRESHOLD, RETRIEVAL_TOP_K
from app.core.config import OLLAMA_MODEL

from app.services.document_processor import get_document_type
from app.services.pdf_parser_service import extract_text_from_pdf
from app.services.ocr_service import extract_text_from_image
from app.services.text_cleaning_service import clean_extracted_text
from app.services.chunking_service import split_text_into_chunks
from app.services.embedding_service import generate_embeddings
from app.services.vector_store_service import store_embeddings
from app.services.retrieval_service import search_similar_chunks

from app.services.llm_service import generate_answer
from app.services.llm_intent_service import classify_intent
from app.services.llm_prompt_service import (
    build_general_prompt,
    build_rag_prompt,
    build_no_context_fallback_prompt,
)
from app.services.logging_service import log_query_interaction

from app.models.question import QuestionRequest



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

    # Generate embeddings for the chunks
    embeddings = generate_embeddings(chunks)

    # Store the embeddings and metadata in the vector database
    file_size = file_path.stat().st_size

    storage_result = store_embeddings(
        chunks=chunks,
        embeddings=embeddings,
        filename=file.filename,
        content_type=file.content_type,
        document_type=document_type,
        language="unknown",
        file_size=file_size,
    )


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
        "number_of_embeddings": len(embeddings),
        "embedding_dimension": len(embeddings[0]) if embeddings else 0,
        "first_chunk_preview": chunks[0][:500] if chunks else None,
        "second_chunk_preview": chunks[1][:500] if len(chunks) > 1 else None,
        "stored_vectors": storage_result["stored_vectors"],
        "sample_stored_record": storage_result["sample_stored_record"],
        "message": "File uploaded successfully.",

    }


@router.post("/ask")
def ask_question(request: QuestionRequest):
    question = request.question.strip()

    if not question:
        return {
            "answer": "Please provide a question.",
            "intent": "empty",
            "results": [],
        }

    intent = classify_intent(question)

    if intent == "general_message":
        prompt = build_general_prompt(question)
        answer = generate_answer(prompt)

        log_query_interaction(
            question=question,
            answer=answer,
            intent=intent,
            model=OLLAMA_MODEL,
            retrieved_chunks=[],
            use_similarity_threshold=request.use_similarity_threshold,
            threshold=MIN_SIMILARITY_THRESHOLD,
        )
        return {
            "answer": answer,
            "intent": intent,
            "results": [],
        }

    retrieved_chunks = search_similar_chunks(
        question=question,
        top_k=RETRIEVAL_TOP_K,
    )

    if request.use_similarity_threshold:
        retrieved_chunks = [
            item for item in retrieved_chunks
            if item["similarity"] >= MIN_SIMILARITY_THRESHOLD
        ]

        if not retrieved_chunks:

            fallback_prompt = build_no_context_fallback_prompt(question)
            answer = generate_answer(fallback_prompt)

            log_query_interaction(
                question=question,
                answer=answer,
                intent=intent,
                model=OLLAMA_MODEL,
                retrieved_chunks=[],
                use_similarity_threshold=request.use_similarity_threshold,
                threshold=MIN_SIMILARITY_THRESHOLD,
            )   
            return {
                "answer": answer,
                "intent": intent,
                "results": [],
                "mode": "threshold_blocked",
                "threshold": MIN_SIMILARITY_THRESHOLD,
            }

    prompt = build_rag_prompt(
        question=question,
        retrieved_chunks=retrieved_chunks,
    )

    answer = generate_answer(prompt)

    log_query_interaction(
        question=question,
        answer=answer,
        intent=intent,
        model=OLLAMA_MODEL,
        retrieved_chunks=retrieved_chunks,
        use_similarity_threshold=request.use_similarity_threshold,
        threshold=MIN_SIMILARITY_THRESHOLD,
    )


    return {
        "answer": answer,
        "intent": intent,
        "results": retrieved_chunks,
        "mode": "rag_with_threshold" if request.use_similarity_threshold else "rag_llm_decision",
    }