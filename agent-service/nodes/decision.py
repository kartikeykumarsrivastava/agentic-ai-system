# nodes/decision.py

def decide_tools(state):
    query = state["query"].lower()

    return {
        "use_rag": "loan" in query or "interest" in query,
        "use_eligibility": "salary" in query or "eligible" in query,
        "use_policy": "policy" in query or "rules" in query
    }