# Function to calculate gross salary
def calculate_gross_salary(hourly_rate, hours_worked):
    return hourly_rate * hours_worked


# Function to calculate all discounts
def calculate_discounts(gross_salary):
    inss = gross_salary * 0.08
    income_tax = gross_salary * 0.11
    union_fee = gross_salary * 0.05

    total = inss + income_tax + union_fee

    return inss, income_tax, union_fee, total


# Function to calculate net salary
def calculate_net_salary(gross_salary, total_discount):
    return gross_salary - total_discount


# Function to display a formatted summary
def summary(hourly_rate, hours_worked):
    gross = calculate_gross_salary(hourly_rate, hours_worked)
    inss, income_tax, union_fee, total = calculate_discounts(gross)
    net = calculate_net_salary(gross, total)

    print("\n" + "=" * 40)
    print("        PAYCHECK SUMMARY")
    print("=" * 40)
    print(f"Gross salary:        ${gross:.2f}")
    print(f"INSS (8%):           ${inss:.2f}") 
    print(f"Income tax (11%):    ${income_tax:.2f}")
    print(f"Union fee (5%):      ${union_fee:.2f}")
    print("-" * 40)
    print(f"Total discount:      ${total:.2f}")
    print(f"Net salary:          ${net:.2f}")
    print("=" * 40)


# Main program
try:
    hourly_rate = float(input("Enter your hourly rate: "))
    hours_worked = float(input("Enter total hours worked this month: "))

    if hourly_rate < 0 or hours_worked < 0:
        print("Values must be positive.")
    else:
        summary(hourly_rate, hours_worked)

except ValueError:
    print("Please enter valid numeric values.")