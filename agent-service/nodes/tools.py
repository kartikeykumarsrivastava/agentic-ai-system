# nodes/tools.py

import requests


#  Retry + Timeout Wrapper
def safe_api_call(url, method="GET", payload=None, retries=2):
    for i in range(retries):
        try:
            if method == "POST":
                res = requests.post(url, json=payload, timeout=3)
            else:
                res = requests.get(url, timeout=3)

            if res.headers.get("content-type", "").startswith("application/json"):
                return res.json()
            return res.text

        except Exception as e:
            print(f"Retry {i+1} failed:", e)
            time.sleep(1)

    return None

def call_rag(state):
    res = requests.post(
        "http://localhost:8001/retrieve",
        json={"query": state["query"]}
    )
    return {"documents": res.json().get("documents", [])}


# nodes/tools.py

from nodes.utils import extract_salary

def call_eligibility(state):
    salary = extract_salary(state["query"])

    payload = {
        "salary": salary,
        "age": 30,  # default for now
        "existing_emi": 10000,
        "credit_score": 750,
        "employment_type": "salaried"
    }


    res = requests.post(
        "http://localhost:8002/check",
        json=payload
    )

    state["eligibility"] = res.json()
    return state

def call_policy(state):
    res = requests.post(
    "http://localhost:8081/policy/query",
    json={"topic": query})