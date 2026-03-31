# rag-service/ingest.py

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from dotenv import load_dotenv
import os

load_dotenv()

documents = []

# 🔹 Load PDF
pdf_loader = PyPDFLoader("data/loan_docs.pdf")
pdf_docs = pdf_loader.load()

for doc in pdf_docs:
    doc.metadata["source"] = "pdf"
documents.extend(pdf_docs)

# 🔹 Load TXT
with open("data/loan_docs.txt") as f:
    text = f.read()

txt_doc = Document(
    page_content=text,
    metadata={"source": "txt"}
)

documents.append(txt_doc)

# 🔹 Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

docs = splitter.split_documents(documents)

# 🔹 Embeddings
embedding = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# 🔹 Vector DB
vector_db = FAISS.from_documents(docs, embedding)

# 🔹 Save index
vector_db.save_local("vector_store/faiss_index")

print("✅ Ingestion complete with PDF + TXT")