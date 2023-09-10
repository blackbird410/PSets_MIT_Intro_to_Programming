

def main():
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))

    print(f"Number of months: {get_months(annual_salary, portion_saved, total_cost)}")


def get_months(annual_salary, portion_saved, total_cost):
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    months = 0
    
    while current_savings < portion_down_payment * total_cost:
        current_savings += (current_savings * r / 12) + (portion_saved * annual_salary / 12)
        months += 1

    return months


if __name__ == "__main__":
    main()