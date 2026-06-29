import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from agent import run_agent
from tools import analyze_expenses
from reports import create_report


st.set_page_config(
    page_title="Personal Finance Assistant",
    page_icon="💰",
    layout="wide"
)

st.sidebar.title("💰 Personal Finance Assistant")

st.sidebar.info(
    """
    Features:

    ✅ Salary Memory  \n
    ✅ Savings Goal Planner \n 
    ✅ Affordability Checker  \n
    ✅ Mutual Fund Search  \n
    ✅ Expense Analysis  \n
    ✅ Expense Charts  \n
    ✅ PDF Report Generation
    """
)


st.title("💰 Personal Finance Assistant Agent")

st.markdown(
    "Plan your finances, analyze expenses, and get investment insights."
)

st.markdown("---") #just for making it look neat

st.header("📂 Upload Expense CSV")

uploaded_file = st.file_uploader(
    "Upload your expense file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    #display the uploaded data
    st.subheader("Uploaded Data")
    st.dataframe(df)

    summary = analyze_expenses(df)

    col1, col2 = st.columns(2)

    with col1:
        st.success(
            f"Total Expenses: Rs. {summary['total']}"
        )

    with col2:
        st.info(
            f"Highest Spending Category: "
            f"{summary['highest_category']}"
        )

    #to give the piechart
    st.subheader("Expense Distribution")

    fig, ax = plt.subplots()

    ax.pie(
        df["Amount"],
        labels=df["Category"],
        autopct="%1.1f%%"
    )

    ax.set_title("Expense Breakdown")

    st.pyplot(fig)

    #to generate pdf report
    report_file = create_report(summary)

    with open(report_file, "rb") as file:

        st.download_button(
            label="📥 Download Financial Report",
            data=file,
            file_name="finance_report.pdf",
            mime="application/pdf"
        )

st.markdown("---")

#chatbot
st.header(" Ask Your Finance Assistant")

user_input = st.text_input(
    "Ask me something..."
)

if st.button("Submit"):

    if user_input.strip() == "":
        st.warning(
            "Please enter a question."
        )

    else:
        result = run_agent(user_input)

        st.success(result)

st.markdown("---")

st.caption(
    "Built using Python, Streamlit, OpenRouter, and Agentic AI."
)