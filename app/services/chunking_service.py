from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import CHUNK_OVERLAP, CHUNK_SIZE


def split_text_into_chunks(text: str) -> list[str]:
    if not text:
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    chunks = splitter.split_text(text)

    return [chunk.strip() for chunk in chunks if chunk.strip()]