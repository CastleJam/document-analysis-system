from datetime import datetime

import chromadb

from app.core.config import COLLECTION_NAME, VECTOR_DB_PATH


client = chromadb.PersistentClient(path=str(VECTOR_DB_PATH))

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={
        "hnsw:space": "cosine"
    }
)


def store_embeddings(
    chunks: list[str],
    embeddings: list[list[float]],
    filename: str,
    content_type: str,
    document_type: str,
    language: str,
    file_size: int,
) -> dict:
    if not chunks or not embeddings:
        return {
            "stored_vectors": 0,
            "sample_stored_record": None,
        }

    ids = []
    metadatas = []
    upload_time = datetime.utcnow().isoformat()

    for index, chunk in enumerate(chunks):
        chunk_number = index + 1

        ids.append(f"{filename}_chunk_{chunk_number}")

        metadatas.append(
            {
                "filename": filename,
                "page_number": "unknown",
                "chunk_id": chunk_number,
                "content_type": content_type,
                "document_type": document_type,
                "language": language,
                "upload_time": upload_time,
                "file_size": file_size,
            }
        )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    sample_stored_record = {
        "id": ids[0],
        "document_preview": chunks[0][:500],
        "embedding_preview": embeddings[0][:10],
        "embedding_dimension": len(embeddings[0]),
        "metadata": metadatas[0],
    }

    return {
        "stored_vectors": len(ids),
        "sample_stored_record": sample_stored_record,
    }