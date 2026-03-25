# agent-service/config/llm.py

from langchain.chat_models import ChatOpenAI
from config.settings import OPENAI_API_KEY, MODEL_NAME

def get_llm():
    return ChatOpenAI(
        model=MODEL_NAME,
        openai_api_key=OPENAI_API_KEY,
        temperature=0
    )