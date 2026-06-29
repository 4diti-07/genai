import json

from llm import ask_llm
from memory import load_memory, save_memory
from finance import *
from tools import *


def run_agent(user_input):

    memory = load_memory()
    responses = []

    text = user_input.lower()

    
    if "salary" in text:

        numbers = [
            int(s)
            for s in text.split()
            if s.isdigit()
        ]

        if numbers:
            salary = numbers[0]

            memory["salary"] = salary
            save_memory(memory)

            responses.append(
                f"Salary saved: ₹{salary:,}"
            )

   
    if "save" in text and "year" in text:

        numbers = [
            int(s)
            for s in text.split()
            if s.isdigit()
        ]

        if len(numbers) >= 2:

            amount = numbers[0]
            years = numbers[1]

            monthly = monthly_savings(
                amount,
                years
            )

            responses.append(
                f"You need to save ₹{monthly:,.2f} per month."
            )

    
    if "emergency fund" in text:

        expenses = memory.get("expenses")

        if expenses:
            fund = emergency_fund(expenses)

            responses.append(
                f"Recommended emergency fund: ₹{fund:,}"
            )
        else:
            responses.append(
                "Please save your monthly expenses first."
            )

   
    try:

        llm_response = ask_llm(user_input)

        print("LLM RESPONSE:")
        print(llm_response)

        if llm_response.startswith("LLM Error"):
            responses.append(llm_response)

        else:
            plan = json.loads(llm_response)

            for action in plan["actions"]:

                tool = action["tool"]
                data = action["input"]

                
                if tool == "search":
                    print("SEARCH QUERY:", data)

                    results = web_search(data)

                    print("SEARCH RESULTS:", results)

                    if len(results) == 0:
                        responses.append(
                            "No search results found."
                        )

                    else:
                        text_result = "Search Results:\n"

                        for r in results:

                            title = r.get(
                                "title",
                                "No Title"
                            )

                            text_result += (
                                f"- {title}\n"
                            )

                        responses.append(
                            text_result
                        )

            
                elif tool == "affordability":

                    salary = memory.get("salary")

                    if salary:

                        price = int(data)

                        result = affordability(
                            salary,
                            price
                        )

                        responses.append(
                            f"Affordability: {result}"
                        )

                    else:
                        responses.append(
                            "Please save your salary first."
                        )

    except Exception as e:
        responses.append(
            f"Error: {str(e)}"
        )

    if len(responses) == 0:
        responses.append(
            "I can help with budgeting, savings goals, affordability checks and financial searches."
        )

    return "\n\n".join(responses)