from fastapi import FastAPI
from graph import graph

app = FastAPI()

@app.post("/ask")
def ask(req: dict):
    try:
        result = graph.invoke({
            "query": req["query"],
            "use_rag": False,
            "use_eligibility": False,
            "use_policy": False
        })
        return {"response": result.get("final_answer")}

    except Exception as e:
        import traceback
        traceback.print_exc()   # 🔥 IMPORTANT
        return {"error": str(e)}