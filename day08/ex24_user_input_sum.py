# Variable that will store the current number entered by the user
number = 0

# Variable that will store the total sum
total = 0

# Infinite loop - will continue running until the user enters 0
while True:

    # Ask the user to enter a number
    number = int(input("Enter a number (0 to stop): "))

    # Check if the user wants to stop the program
    if number == 0:
        break  # Exit the loop

    # Add the number to the total
    total += number

    # Show the current total after adding the number
    print(f"Current total: {total}")