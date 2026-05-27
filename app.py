import streamlit as st
import os

from src.pdf_loader import load_pdfs
from src.text_chunker import chunk_texts
from src.embedding_store import create_vector_store, add_to_vector_store
from src.rag_chain import create_rag_chain

# -----------------------------
# CONFIG
# -----------------------------
PDF_DIR = "data/pdfs"
os.makedirs(PDF_DIR, exist_ok=True)

st.set_page_config(page_title="RAG Chat With PDFs", layout="wide")

st.title("📚 Chat With Your Documents (RAG)")

# -----------------------------
# SESSION STATE
# -----------------------------
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

# -----------------------------
# FILE UPLOAD SECTION
# -----------------------------
st.subheader("📂 Upload PDFs")

uploaded_files = st.file_uploader(
    "Upload one or more PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Process PDFs"):

    if not uploaded_files:
        st.warning("Please upload at least one PDF.")
        st.stop()

    # -----------------------------
    # SAFE FILE HANDLING (FIXED)
    # -----------------------------
    for filename in os.listdir(PDF_DIR):
        file_path = os.path.join(PDF_DIR, filename)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Could not delete {file_path}: {e}")

    # Save uploaded PDFs
    for file in uploaded_files:
        file_path = os.path.join(PDF_DIR, file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())

    st.info("Loading PDFs...")

    # Load → Chunk → Embed
    docs = load_pdfs(PDF_DIR)
    chunks = chunk_texts(docs)

    st.info("Creating embeddings & vector store...")

    # Create or update vector store
    if st.session_state.vector_store is None:
        st.session_state.vector_store = create_vector_store(chunks)
    else:
        st.session_state.vector_store = add_to_vector_store(
            st.session_state.vector_store,
            chunks
        )

    st.success("PDFs processed successfully!")

    # Create RAG chain
    st.session_state.rag_chain = create_rag_chain(
        st.session_state.vector_store.as_retriever()
    )

# -----------------------------
# CHAT SECTION
# -----------------------------
st.subheader("💬 Ask questions")

query = st.text_input("Ask something from your PDFs")

if st.button("Ask"):

    if st.session_state.rag_chain is None:
        st.warning("Please upload and process PDFs first.")
        st.stop()

    if not query:
        st.warning("Enter a question.")
        st.stop()

    with st.spinner("Thinking..."):
        response = st.session_state.rag_chain.invoke(
            {"question": query}
        )

    st.write("### Answer")
    st.write(response["answer"])