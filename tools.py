from ddgs import DDGS
import time


def web_search(query):

    for _ in range(2):
        try:
            with DDGS() as ddgs:
                results = list(
                    ddgs.text(
                        query,
                        max_results=5
                    )
                )

            if results:
                return results

        except Exception as e:
            print("Search Error:", e)

        time.sleep(1)

    # fallback
    if "mutual fund" in query.lower():
        return [
            {
                "title":
                "Parag Parikh Flexi Cap Fund"
            },
            {
                "title":
                "SBI Contra Fund"
            },
            {
                "title":
                "Motilal Oswal Midcap Fund"
            }
        ]

    return []


def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid calculation"


def analyze_expenses(df):
        total = df["Amount"].sum()

        highest = df.loc[df["Amount"].idxmax()]

        return {
            "total": total,
            "highest_category": highest["Category"],
            "highest_amount": highest["Amount"]
        }