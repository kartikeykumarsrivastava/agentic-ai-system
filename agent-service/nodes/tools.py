# nodes/tools.py

import requests

def call_rag(state):
    res = requests.post(
        "http://localhost:8001/retrieve",
        json={"query": state["query"]}
    )
    return {"documents": res.json().get("documents", [])}


def call_eligibility(state):
    res = requests.post(
        "http://localhost:8002/check",
        json={"salary": 800000}
    )
    return {"eligibility": res.json()}


def call_policy(state):
    res = requests.get("http://localhost:8081/policy")
    return {"policy": res.text}