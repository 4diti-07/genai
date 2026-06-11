from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your api key"
)

try:
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "user", "content": "What is recursion?"}
        ]
    )

    print(response.choices[0].message.content)

except Exception as e:
    print(e)