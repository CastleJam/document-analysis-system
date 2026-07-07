from sentence_transformers import SentenceTransformer

from app.core.config import EMBEDDING_MODEL
from app.services.vector_store_service import collection


# Load embedding model
embedding_model = SentenceTransformer(EMBEDDING_MODEL)


def search_similar_chunks(question: str, top_k: int = 5):

    question_embedding = embedding_model.encode(
        question,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).tolist()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k,
    )

    formatted_results = []

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):

        similarity = round((1 - distance)  , 4)

        formatted_results.append(
            {
                "distance": round(distance, 4),
                "similarity": similarity,
                "filename": metadata["filename"],
                "page_number": metadata["page_number"],
                "chunk_id": metadata["chunk_id"],
                "document_type": metadata["document_type"],
                "language": metadata["language"],
                "upload_time": metadata["upload_time"],
                "chunk": document,
            }
        )

    return formatted_results