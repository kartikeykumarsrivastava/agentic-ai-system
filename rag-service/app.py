# rag-service/app.py

from fastapi import FastAPI
from pydantic import BaseModel
from retriever import retreive_docs

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/retrieve")
def retrieve(req: QueryRequest):
    docs = retreive_docs(req.query)
    return {"documents": docs}