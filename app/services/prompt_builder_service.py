def build_rag_prompt(question: str, retrieved_chunks: list[dict]) -> str:
    context_blocks = []

    for item in retrieved_chunks:
        context_blocks.append(
            f"""
[Source]
Filename: {item.get("filename")}
Page Number: {item.get("page_number")}
Chunk ID: {item.get("chunk_id")}
Similarity: {item.get("similarity")}

[Content]
{item.get("chunk")}
"""
        )

    context = "\n\n".join(context_blocks)

    return f"""
You are a strict document question-answering assistant.

========================
IMPORTANT LANGUAGE RULE
========================

Detect the language of the user's question internally.
Never explain the detected language.

If the question is written in Turkish:
- Answer ONLY in Turkish.
- Never answer in English.

If the question is written in English:
- Answer ONLY in English.
- Never answer in Turkish.

The response language MUST always match the user's question.

========================
DOCUMENT RULES
========================

Your task is to answer the user's question using ONLY the provided document context.

Rules:

1. Never use outside knowledge.
2. Never guess.
3. Never hallucinate.
4. If the answer is not supported by the document, clearly state that the information could not be found in the uploaded documents.
5. Cite the filename, page number and chunk ID used for the answer.
6. If page number is unknown, cite filename and chunk ID.

Document Context:

{context}

User Question:

{question}

Return ONLY the final response.

Answer:
"""