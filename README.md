# Document Analysis System

AI-powered document analysis and question answering system using Retrieval-Augmented Generation (RAG).

The system allows users to upload PDF or image documents, indexes them using Retrieval-Augmented Generation (RAG), and answers questions based on the uploaded documents content. The application is allow users to chat or ask general questions, in such scenario the system response without needing to look up the uploaded documents content.

---

# Demo Video

You may find the demo video here: https://www.loom.com/share/0123c912bea740849cf5754992771844

---


# System Architecture and Flow Chart

You may find the related documents under the docs folder.



# Technologies

| Component | Technology |
|-----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| OCR | Tesseract |
| PDF Parsing | pdfplumber |
| Embedding Model | sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 |
| Vector Database | ChromaDB |
| Local LLM | Llama 3.1 8B 128K |
| Chunking | LangChain RecursiveCharacterTextSplitter |



# Installation

## 1. Install Python

Install **Python 3.11 or later**.

Download:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

Expected output:

```text
Python 3.11.x
```

## 2. Clone Repository

```bash
git clone https://github.com/CastleJam/document-analysis-system.git

cd document-analysis-system
```

---

## 3. Create and Activate Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Install Tesseract OCR

Install Tesseract OCR and make sure it is available in your system PATH:


https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0

---

## 6. Install Ollama

Download and install Ollama.

https://ollama.com

For Linux / macOS, Start Ollama:

```bash
ollama serve
```


Pull the required model:

```bash
ollama pull llama3.1:latest
```

See it is available:
```bash
ollama list
```

---

# Running the Backend

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# Running the Frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

# Usage

1. Upload a PDF or image document.
2. Wait until document processing is completed.
3. Write anything. Ask questions about the uploaded documents.
4. The system retrieves the most relevant chunks from Vector Database.
5. The LLM generates an answer only from the retrieved document context.

---

# Documentation

- README.md — Project overview and setup instructions
- DEVLOG.md — Development decisions and engineering process
- TESTING.md — Test scenarios and validation results

