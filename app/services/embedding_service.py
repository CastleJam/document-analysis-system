from sentence_transformers import SentenceTransformer

from app.core.config import EMBEDDING_MODEL

# Load the embedding model once during application startup.
embedding_model = SentenceTransformer(EMBEDDING_MODEL)


def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    """
    Generate vector embeddings for a list of text chunks.
    """

    if not chunks:
        return []

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    return embeddings.tolist()