import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant" # Reference: https://python.langchain.com/api_reference/groq/chat_models/langchain_groq.chat_models.ChatGroq.html