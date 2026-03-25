# Loan approval system based on salary and house value

# User input
try:
    house_value = float(input("How much is the price of the house? $"))
    salary = float(input("Insert your salary: $"))
    years = int(input("What is the quantity of the years? "))

    # Validate input to avoid invalid calculations
    if years <= 0:
        print("Invalid number of years.")
    else:
        # Convert years to months
        months = years * 12

        # Calculate monthly payment
        monthly_payment = house_value / months

        # Calculate maximum allowed payment (30% of salary)
        limit_value = salary * 0.30

        # Decision logic
        if monthly_payment <= limit_value:
            print("\nLoan approved.")
        else:
            print("\nLoan denied.")

        # Display detailed information
        print("\n--- DETAILS ---")
        print(f"Salary: ${salary:.2f}")
        print(f"Allowed limit (30%): ${limit_value:.2f}")
        print(f"Monthly payment: ${monthly_payment:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")