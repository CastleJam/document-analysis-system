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

VECTOR_DB_PATH = BASE_DIR / "vector_db"

COLLECTION_NAME = "document_chunks"

OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.1:latest"

RETRIEVAL_TOP_K = 5
MIN_SIMILARITY_THRESHOLD = 0.6

LOG_DIR = BASE_DIR / "logs"
QUERY_LOG_FILE = LOG_DIR / "query_logs.jsonl"