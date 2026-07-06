from pathlib import Path

APP_NAME = "Document Analysis System"
APP_DESCRIPTION = "AI-powered document analysis and question answering system using Retrieval-Augmented Generation (RAG)."
APP_VERSION = "0.1.0"

BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"

ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 300

EMBEDDING_MODEL = (
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)