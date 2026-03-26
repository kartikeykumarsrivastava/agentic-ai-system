# graph.py

from langgraph.graph import StateGraph
from state import AgentState

from nodes.decision import decide_tools
from nodes.tools import call_rag, call_eligibility, call_policy
from nodes.response import generate_response


# Initialize Graph
builder = StateGraph(AgentState)


# 🔹 Register Nodes
builder.add_node("decide", decide_tools)
builder.add_node("rag", call_rag)
builder.add_node("eligibility", call_eligibility)
builder.add_node("policy", call_policy)
builder.add_node("response", generate_response)


# 🔹 Entry Point
builder.set_entry_point("decide")


# 🧠 Conditional Routing (SEQUENTIAL - FIXED)
def route_tools(state):
    """
    Decide which tool to call based on query intent.
    IMPORTANT: Returns only ONE node to avoid parallel state conflicts.
    """

    # Priority-based routing
    if state.get("use_eligibility"):
        return "eligibility"

    elif state.get("use_policy"):
        return "policy"

    elif state.get("use_rag"):
        return "rag"

    else:
        return "response"


# 🔹 Attach Conditional Edges
builder.add_conditional_edges(
    "decide",
    route_tools
)


# 🔹 Define Flow to Response
builder.add_edge("rag", "response")
builder.add_edge("eligibility", "response")
builder.add_edge("policy", "response")


# 🔹 Compile Graph
graph = builder.compile()