# nodes/response.py

from langchain_openai import ChatOpenAI
from config import MODEL_NAME, OPENAI_API_KEY

llm = ChatOpenAI(
    model=MODEL_NAME,
    openai_api_key=OPENAI_API_KEY
)

def generate_response(state):
    prompt = f"""
    User Query: {state['query']}

    Documents: {state.get('documents')}
    Eligibility: {state.get('eligibility')}
    Policy: {state.get('policy')}

    Provide a clear structured answer.
    """

    response = llm.invoke(prompt)

    return {"final_answer": response.content}