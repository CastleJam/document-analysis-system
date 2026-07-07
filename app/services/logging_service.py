import json
from datetime import datetime

from app.core.config import LOG_DIR, QUERY_LOG_FILE


def log_query_interaction(
    question: str,
    answer: str,
    intent: str,
    model: str,
    retrieved_chunks: list[dict],
    use_similarity_threshold: bool,
    threshold: float,
) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    log_record = {
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "answer": answer,
        "intent": intent,
        "model": model,
        "use_similarity_threshold": use_similarity_threshold,
        "threshold": threshold,
        "retrieved_chunks": [
            {
                "filename": item.get("filename"),
                "page_number": item.get("page_number"),
                "chunk_id": item.get("chunk_id"),
                "similarity": item.get("similarity"),
                "document_type": item.get("document_type"),
                "language": item.get("language"),
            }
            for item in retrieved_chunks
        ],
    }

    with QUERY_LOG_FILE.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(log_record, ensure_ascii=False) + "\n")