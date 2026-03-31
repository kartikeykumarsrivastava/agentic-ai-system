from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini")

embedding = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY
)

vector_db = FAISS.load_local("vector_store/faiss_index", embedding, allow_dangerous_deserialization =True)

def rerank(query, docs):
    # Placeholder for a more complex reranking logic, e.g., using a language model

    prompt = f"""
    You are a ranking system.

    Query: {query}

    Documents:
    {docs}

    Select the top 2 most relevant documents.

    STRICT RULES:
    - Return ONLY a Python list
    - No explanation
    - No numbering
    - No extra text

    Example output:
    ["doc1", "doc2"]
    """
    response = llm.invoke(prompt)

    try:
        return eval(response.content)
    except:
        return docs[:2]



def retreive_docs(query:str, k=3):
    results = vector_db.similarity_search(query, k=k)
    docs= [doc.page_content for doc in results]

    reranked_docs = rerank(query, docs)

    return reranked_docs
