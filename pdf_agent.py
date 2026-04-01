# pdf_agent.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

def create_pdf_agent(pdf_path):

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    # Vector DB
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever()

    # LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0.7,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # 🔥 Custom QA function (replacement for RetrievalQA)
    def ask(query):

        retrieved_docs = retriever.get_relevant_documents(query)

        context = "\n".join([doc.page_content for doc in retrieved_docs])

        prompt = f"""
        Answer the question using the context below:

        {context}

        Question: {query}
        """

        return llm.invoke(prompt).content

    return ask