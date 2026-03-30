#Monthly Financial Summary 
income = float(input("What's your income ($)?"))
expenses = float(input("And your expenses ($)?"))

#Calculate monthly balance
balance = income - expenses

# Display formatted financial summary
print("\n=== MONTHLY SUMMARY === ")
print(f"Incomes: ${income:.2f}")
print(f"Expenses: ${expenses:.2f}")
print(f"Balance: ${balance:.2f}")

print("=========================")