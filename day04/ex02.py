#Salary calculator

try:
   
    hourlyRate = float(input("How much do you earn per hour? "))

    
    hoursWorked = float(input("How many hours did you work this month? "))
    
    # Calculate gross salary
    grossSalary = hourlyRate * hoursWorked

    # Calculate each discount
    inss = grossSalary * 0.08
    incomeTax = grossSalary * 0.11
    unionFee = grossSalary * 0.05

    # Calculate total discount
    totalDiscount = inss + incomeTax + unionFee

    # Calculate net salary
    netSalary = grossSalary - totalDiscount

    # Show paycheck summary
    print("==== PAYCHECK SUMMARY ====")
    print(f"Gross salary:        ${grossSalary:.2f}")
    print(f"INSS (8%):           ${inss:.2f}") 
    print(f"Income tax (11%):    ${incomeTax:.2f}")
    print(f"Union fee (5%):      ${unionFee:.2f}")
    print(f"Total discount:      ${totalDiscount:.2f}")
    print(f"Net salary:          ${netSalary:.2f}")
    print("==========================")

# Handle invalid input
except ValueError:
    print("Please enter valid numbers.")