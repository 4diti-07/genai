from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def ask_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content":
                    """
                    You are an AI Personal Finance Agent.

                    Available tools:
                    - search
                    - affordability

                    Return ONLY valid JSON.

                    Example:

                    {
                      "actions":[
                        {
                          "tool":"search",
                          "input":"best mutual funds in India"
                        }
                      ]
                    }
                    """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"LLM Error: {e}"