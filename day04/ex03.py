# Paint Store Calculator

try:

    totalArea = float(input("Enter the total area (m²): "))
    
    pricePerCan = 80
    
    # Calculate liters needed (1 liter covers 3 m²)
    litersNeeded = totalArea / 3 
    
    # Calculate base number of cans (each can has 18 liters)
    cansNeeded = int(litersNeeded / 18)
    
    # If there is remainder, add one more can
    if litersNeeded % 18 != 0:
        cansNeeded += 1
    
    # Calculate total price
    totalPrice = cansNeeded * pricePerCan

    # Show results
    print("==== TOTAL ====")
    print(f"Total area:           {totalArea:.2f} m²")
    print(f"Price per can:       ${pricePerCan:.2f}")
    print(f"Cans needed:         {cansNeeded}")
    print(f"Total price:         ${totalPrice:.2f}")

# Handle invalid input
except ValueError:
    print("Please enter a valid number")