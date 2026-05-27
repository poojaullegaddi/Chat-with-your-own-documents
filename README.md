# 📚 Chat With Your PDFs (RAG AI Assistant)

A Retrieval-Augmented Generation (RAG) based AI chatbot that allows users to upload PDF documents and ask questions about their content. The system retrieves relevant context from documents and generates accurate answers using a Large Language Model (LLM).

---

# 🚀 Features

- 📂 Upload multiple PDF files
- 🧠 Ask questions in natural language
- 🔍 Semantic search using FAISS
- ⚡ Fast responses using Groq LLM
- 💬 Conversational memory support
- 📄 Answers based only on your documents

---

# 🧠 How It Works

PDF Upload  
→ Text Extraction (PyPDF)  
→ Chunking (Text Splitter)  
→ Embeddings (Sentence Transformers)  
→ Vector Store (FAISS)  
→ Retriever (Similarity Search)  
→ LLM (Groq - LLaMA3)  
→ Final Answer  

---

# 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS (Vector Database)
- HuggingFace Embeddings
- Groq API (LLaMA3)
- PyPDF

---
