# Fish weight control system
# This program calculates the excess weight and the fine to be paid
# if the fish weight exceeds the legal limit (50 kg).

try:
    # Ask the user to enter the fish weight
    fish_weight = float(input("Enter the fish weight (limit is 50 kg): "))

    # Check if the weight exceeds the limit
    if fish_weight > 50:
        excess = fish_weight - 50
        fine = excess * 4  # $4 per kg exceeded

        print("The fish weight exceeds the legal limit.")
        print("==== TOTAL ====")
        print(f"Fish weight: {fish_weight:.2f} kg")
        print(f"Excess weight: {excess:.2f} kg")
        print(f"Fine to pay: ${fine:.2f}")
        print("===============")

    else:
        excess = 0
        fine = 0

        print("The fish weight is within the legal limit.")
        print("==== TOTAL ====")
        print(f"Fish weight: {fish_weight:.2f} kg")
        print(f"Excess weight: {excess:.2f} kg")
        print(f"Fine to pay: ${fine:.2f}")
        print("===============")

# Handle invalid input
except ValueError:
    print("Please enter a valid numeric value.")