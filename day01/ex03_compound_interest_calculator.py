# Simple Interest Calculator

initial_value = float(input("What's the value you want to invest? "))
tax = float(input("What's the tax rate? (example: 0.05) "))
years = int(input("How many years? "))

# Calculate the final balance using compound interest formula
# Formula: Final Balance = Initial Value * (1 + Rate) ^ Time
finalBalance = initial_value * (1 + tax) ** years

# Display the result formatted with 2 decimal places
print(f"In {years} years, your balance will be ${finalBalance:.2f}")