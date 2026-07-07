from app.services.llm_service import generate_answer


def classify_intent(user_message: str) -> str:
    prompt = f"""
You are an intent classifier for a document question-answering system.

Classify the user message into exactly one of these labels:

- general_message
- document_question

Definitions:
general_message: greetings, small talk, help requests, or general chat not asking about uploaded documents.
document_question: any question that asks about uploaded documents, document content, extracted information, summaries, tables, dates, names, or facts from files.

Return only one label. Do not explain.

User message:
{user_message}

Intent:
"""

    result = generate_answer(prompt).strip().lower()

    if "document_question" in result:
        return "document_question"

    if "general_message" in result:
        return "general_message"

    # Safe fallback: if uncertain, treat it as document question.
    return "document_question"