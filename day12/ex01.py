# Create an empty list to store the numbers
numbers = []

# Main program loop (runs until the user chooses to exit)
while True:

    # Display menu options
    print("\n[1] Add numbers")
    print("[2] Show numbers")
    print("[3] Show highest number")
    print("[4] Show lowest number")
    print("[5] Exit")

    # Ask the user to choose an option
    # .strip() removes extra spaces from the input
    choice = input("Choose an option: ").strip()

    # Option 1: Add numbers to the list
    if choice == "1":

        # Ask the user for a number (0 stops the input loop)
        num = int(input("Insert numbers (0 to exit): "))

        # Keep asking for numbers until the user enters 0
        while num != 0:
            numbers.append(num)  # Add the number to the list
            num = int(input("Insert numbers (0 to exit): "))

    # Option 2: Show all numbers in sorted order
    elif choice == "2":

        # Check if the list is not empty
        if numbers:
            print(sorted(numbers))  # Display numbers sorted
        else:
            print("No numbers added yet.")

    # Option 3: Show the highest number
    elif choice == "3":

        # Only works if the list has numbers
        if numbers:
            print("Highest number:", max(numbers))
        else:
            print("No numbers added yet.")

    # Option 4: Show the lowest number
    elif choice == "4":

        # Only works if the list has numbers
        if numbers:
            print("Lowest number:", min(numbers))
        else:
            print("No numbers added yet.")

    # Option 5: Exit the program
    elif choice == "5":

        print("Goodbye!")
        break  # Break the loop and end the program