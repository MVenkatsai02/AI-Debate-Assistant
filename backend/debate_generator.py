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
    Generate a structured debate with at least 10 arguments for and against.
    """
    if not GROQ_API_KEY:
        return "Error: GROQ_API_KEY is missing. Please check your .env file."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # Structured prompt for better formatting
    prompt = f"""
    Debate Topic: {topic}

    **For the Motion (Supporting Arguments):**
    1. [Provide strong supporting argument]
    2. [Provide strong supporting argument]
    3. [Provide strong supporting argument]
    4. [Provide strong supporting argument]
    5. [Provide strong supporting argument]
    6. [Provide strong supporting argument]
    7. [Provide strong supporting argument]
    8. [Provide strong supporting argument]
    9. [Provide strong supporting argument]
    10. [Provide strong supporting argument]

    **Against the Motion (Opposing Arguments):**
    1. [Provide strong opposing argument]
    2. [Provide strong opposing argument]
    3. [Provide strong opposing argument]
    4. [Provide strong opposing argument]
    5. [Provide strong opposing argument]
    6. [Provide strong opposing argument]
    7. [Provide strong opposing argument]
    8. [Provide strong opposing argument]
    9. [Provide strong opposing argument]
    10. [Provide strong opposing argument]

    **Counterarguments & Rebuttals:**
    - [Provide key rebuttal to one argument]
    - [Provide key rebuttal to another argument]
    - [Provide another key rebuttal]

    Conclude with a balanced summary.
    """

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a structured debate assistant. Provide a well-organized debate with at least 10 arguments for and against."},
            {"role": "user", "content": prompt}
        ]
    }

    # Make API request
    response = requests.post(GROQ_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: Failed to fetch response. {response.text}"
