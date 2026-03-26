from fastapi import FastAPI
from pydantic import BaseModel
from graph import graph

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.post("/ask")
def ask(req: QueryRequest):
    result = graph.invoke({
        "query": req.query,
        "use_rag": False,
        "use_eligibility": False,
        "use_policy": False,
        "documents": [],
        "eligibility": {},
        "policy": ""
    })

    return {"response": result.get("final_answer")}