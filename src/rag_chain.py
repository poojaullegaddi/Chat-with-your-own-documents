from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()


def create_rag_chain(retriever):

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.1-8b-instant",
        temperature=0
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=True
    )

    return chain