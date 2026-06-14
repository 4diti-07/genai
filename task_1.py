from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your api key"
)

print("\n===== AI STUDY ASSISTANT =====")

print("\nChoose a Feature:")
print("1. Explain a Concept")
print("2. Summarize Text")
print("3. Generate Quiz Questions")
print("4. Explain Like I'm 5")

choice = input("\nEnter your choice (1-4): ")
text = input("\nEnter your text: ")

# Handle empty input
if text.strip() == "":
    print("Error: Input cannot be empty.")
    exit()

# Custom prompts
if choice == "1":
    prompt = f"Explain the following concept clearly for a college student:\n\n{text}"

elif choice == "2":
    prompt = f"Summarize the following text into bullet points:\n\n{text}"

elif choice == "3":
    prompt = f"Generate 5 quiz questions with answers from the following text:\n\n{text}"

elif choice == "4":
    prompt = f"Explain the following as if teaching a 5-year-old child:\n\n{text}"

else:
    print("Invalid choice.")
    exit()

print("\nGenerating response...\n")

try:
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("===== RESPONSE =====\n")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", e)
