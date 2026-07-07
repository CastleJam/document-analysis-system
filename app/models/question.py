from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str
    use_similarity_threshold: bool = True