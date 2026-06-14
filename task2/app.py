from prompts import get_prompt
from llm_client import get_response

def main():
    print("===== LLM PROMPT APP =====")

    user_input = input("Enter your text: ").strip()

    if not user_input:
        print("Error: Input cannot be empty")
        return

    print("\nChoose Mode:")
    print("1. Teacher Mode")
    print("2. Summarize")
    print("3. Interview Questions")
    print("4. Study Plan")
    print("5. Professional Rewrite")

    mode = input("Enter mode: ")

    prompt = get_prompt(mode, user_input)

    print("\nGenerating response...\n")

    result = get_response(prompt)

    print("\nOUTPUT:\n")
    print(result)

if __name__ == "__main__":
    main()