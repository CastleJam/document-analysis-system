import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Document Analysis System",
    page_icon="📄",
    layout="centered",
)

st.title("📄 Document Analysis System")
st.write("Upload a PDF or image document and ask questions based on its content.")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "jpg", "jpeg", "png"],
)

if uploaded_file is not None:
    if st.button("Process Document"):
        with st.spinner("Uploading and processing document..."):
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type,
                )
            }

            response = requests.post(
                f"{API_BASE_URL}/upload",
                files=files,
                timeout=300,
            )

            if response.status_code == 200:
                st.success("Document uploaded and processed successfully.")
                st.session_state["document_uploaded"] = True
            else:
                st.error("Document upload failed.")
                st.write(response.text)

st.divider()

st.subheader("Ask a question")

question = st.text_input("Enter your question about the uploaded document")

use_threshold = st.checkbox(
    "Use similarity threshold",
    value=True,
)

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            payload = {
                "question": question,
                "use_similarity_threshold": use_threshold,
            }

            response = requests.post(
                f"{API_BASE_URL}/ask",
                json=payload,
                timeout=300,
            )

            if response.status_code == 200:
                data = response.json()

                st.subheader("Answer")
                st.write(data.get("answer", ""))

                results = data.get("results", [])

                if results:
                    st.subheader("Sources")
                    for item in results:
                        st.markdown(
                            f"""
                            **Filename:** {item.get("filename")}  
                            **Page:** {item.get("page_number")}  
                            **Chunk ID:** {item.get("chunk_id")}
                            """
                        )
            else:
                st.error("Question answering failed.")
                st.write(response.text)