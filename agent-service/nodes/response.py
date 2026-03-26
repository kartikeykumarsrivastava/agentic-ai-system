# nodes/response.py

from langchain_openai import ChatOpenAI
from config import MODEL_NAME, OPENAI_API_KEY

llm = ChatOpenAI(
    model=MODEL_NAME,
    openai_api_key=OPENAI_API_KEY
)
def generate_response(state):
    prompt = f"""
You are a banking assistant.

User Query:
{state['query']}

Available Data:
- Documents: {state.get('documents')}
- Eligibility: {state.get('eligibility')}
- Policy: {state.get('policy')}

Instructions:
1. Use ONLY the provided data
2. If eligibility exists → explain clearly
3. If policy exists → summarize
4. DO NOT say "Not Found"
5. If data missing → skip it

Provide a structured answer.
"""

    response = llm.invoke(prompt)

    state["final_answer"] = response.content
    return state