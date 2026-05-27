from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_store(chunks):
    texts = [doc.page_content for doc in chunks]

    vectorstore = FAISS.from_texts(
        texts,
        embedding=embedding_model
    )

    return vectorstore


def add_to_vector_store(vectorstore, chunks):
    texts = [doc.page_content for doc in chunks]
    vectorstore.add_texts(texts)
    return vectorstore