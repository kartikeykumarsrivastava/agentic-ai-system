# nodes/decision.py

def decide_tools(state):
    query = state["query"].lower()

    return {
        "use_rag": True,  # always helpful
        "use_eligibility": any(word in query for word in ["salary", "eligible", "earn", "income"]),
        "use_policy": any(word in query for word in ["policy", "rules", "process"])
    }