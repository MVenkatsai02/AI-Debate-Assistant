import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key from .env file
GROQ_API_KEY = os.getenv("Groq_api_key")

# Groq API URL (Chat Completion Endpoint)
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_debate(topic):
    """
    Generate structured arguments and rebuttals using Groq AI model.
    """
    if not GROQ_API_KEY:
        return {"error": "GROQ_API_KEY is missing. Please check your .env file."}

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",  # Use the correct Groq model
        "messages": [
            {"role": "system", "content": "You are a debate assistant. Generate structured pro and con arguments."},
            {"role": "user", "content": f"Generate a detailed debate on: {topic}"}
        ]
    }

    # Make API request
    response = requests.post(GROQ_API_URL, json=payload, headers=headers)
    return response.json()  # Return API response
