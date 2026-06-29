from fpdf import FPDF

def create_report(summary):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(
        200,
        10,
        txt="Personal Finance Report",
        ln=True
    )

    pdf.ln(10)

    pdf.cell(
        200,
        10,
        txt=f"Total Expenses: Rs. {summary['total']}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Highest Spending Category: {summary['highest_category']}",
        ln=True
    )

    pdf.output("finance_report.pdf")

    return "finance_report.pdf"