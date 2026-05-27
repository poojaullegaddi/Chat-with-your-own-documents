from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdfs(pdf_dir):
    documents = []

    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            file_path = os.path.join(pdf_dir, file)

            loader = PyPDFLoader(file_path)
            docs = loader.load()

            documents.extend(docs)

    return documents