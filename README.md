Personal Finance Assistant Agent - An Agentic AI Task

what do you understand by agentic ai?
Agentic AI refers to artificial intelligence that can set its own goals, plan steps, and take action to get things done without constant human supervision. An Agentic AI-powered Personal Finance Assistant built using Python, Streamlit, and OpenRouter LLMs. The application helps users manage finances, set savings goals, analyze expenses, and receive financial insights through an interactive chat interface.

# Features

1.AI Finance Assistant
2.Expense Analysis
3.Report Generation
4.Agentic AI Capabilities

# Tech Stack
* Python
* Streamlit
* OpenRouter API
* Pandas
* Matplotlib
* FPDF
* DDGS (DuckDuckGo Search)

# Structure

PersonalFinanceAgent/
│
├── app.py
├── agent.py
├── llm.py
├── finance.py
├── memory.py
├── memory.json
├── tools.py
├── reports.py
└── README.md
and .env file

# Run the Application
streamlit run app.py

# Sample Expense CSV

type:csv
Category,Amount
Food,5000
Travel,2000
Shopping,3000
Rent,12000
Entertainment,1500
Healthcare,2500
Utilities,1800


# Example Queries

My salary is 50000

Can I afford a 15000 phone?

I want to save 500000 in 3 years

Search best mutual funds in India

