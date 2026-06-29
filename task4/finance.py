def monthly_savings(goal_amount, years):
    months = years * 12
    return round(goal_amount / months, 2)


def affordability(income, price):
    if price <= income * 0.3:
        return "Affordable"

    elif price <= income:
        return "Possible, but think carefully."

    else:
        return "Not affordable."


def emergency_fund(monthly_expenses):
    return monthly_expenses * 6