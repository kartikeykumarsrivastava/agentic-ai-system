# graph.py

from langgraph.graph import StateGraph
from state import AgentState

from nodes.decision import decide_tools
from nodes.tools import call_rag, call_eligibility, call_policy
from nodes.response import generate_response

builder = StateGraph(AgentState)

# Nodes
builder.add_node("decide", decide_tools)
builder.add_node("rag", call_rag)
builder.add_node("eligibility", call_eligibility)
builder.add_node("policy", call_policy)
builder.add_node("response", generate_response)

# Entry
builder.set_entry_point("decide")

# Conditional routing
def route_tools(state):
    routes = []

    if state["use_rag"]:
        routes.append("rag")
    if state["use_eligibility"]:
        routes.append("eligibility")
    if state["use_policy"]:
        routes.append("policy")

    return routes if routes else ["response"]

builder.add_conditional_edges(
    "decide",
    route_tools
)

# After tools → response
builder.add_edge("rag", "response")
builder.add_edge("eligibility", "response")
builder.add_edge("policy", "response")

graph = builder.compile()