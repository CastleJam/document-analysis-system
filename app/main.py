from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Document Analysis System API is running."
    }