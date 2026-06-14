import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def get_response(prompt):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Prompt Mode App"
    }

    data = {
        "model": "openrouter/owl-alpha",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=30
    )

    if response.status_code != 200:
        return f"API Error\n\n{response.text}"

    result = response.json()

    return result["choices"][0]["message"]["content"]