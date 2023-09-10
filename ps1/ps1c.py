from math import floor

def main():
    annual_salary = int(input("Enter your annual salary: "))

    savings_rate, steps = get_savings_rate(annual_salary)

    print(f"Best savings rate: {savings_rate}\nSteps in bissection search: {steps}")


def get_savings_rate(annual_salary):
    semi_annual_raise = 0.07
    portion_down_payment = 0.25
    total_cost = 1000000
    r = 0.04
    months = 36
    records = []
    max_rate = 10000
    min_rate = 0
    current_savings = 0
    steps = 0
    
    while abs(current_savings - portion_down_payment * total_cost) > 100:
        current_savings = 0
        salary = annual_salary
        portion_saved = floor((max_rate + min_rate) / 2) / 10000

        if portion_saved in records:
            return "It is not possible to pay the down payment in three years.", steps

        for i in range(1, months + 1):
            current_savings += (current_savings * r / 12) + (portion_saved * salary / 12)
            if not i % 6:
                    salary *= (1 + semi_annual_raise)

        # Start bissection algorithm
        if current_savings > portion_down_payment * total_cost:
            max_rate = (max_rate + min_rate) / 2 
        else:
            min_rate = (max_rate + min_rate) / 2

        records.append(portion_saved)
        steps += 1

    return str(portion_saved), steps





if __name__ == "__main__":
    main()