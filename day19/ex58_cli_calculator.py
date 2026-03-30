# Function to ask the user for two numbers
def get_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    return num1, num2


# Function to add two numbers
def add():
    num1, num2 = get_numbers()

    total = num1 + num2
    
    print(f"\nResult: {total}\n")


# Function to subtract two numbers
def subtract():
    num1, num2 = get_numbers()

    total = num1 - num2

    print(f"\nResult: {total}\n")


# Function to divide two numbers
def divide():
    num1, num2 = get_numbers()

    # Prevent division by zero
    if num2 == 0:
        print("\nError: Cannot divide by zero.\n")
    else:
        total = num1 / num2
        print(f"\nResult: {total:.2f}\n")


# Function to multiply two numbers
def multiply():
    num1, num2 = get_numbers()

    total = num1 * num2

    print(f"\nResult: {total}\n")


# Main program loop
while True:

    # Display calculator menu
    print("\n========== CLI Calculator ==========")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Exit")
    print("====================================")

    # Ask the user to choose an option
    user_choice = input("Select an option: ")

    if user_choice == "5":
        print("\nCalculator closed.")
        break

    elif user_choice == "1":
        add()

    elif user_choice == "2":
        subtract()

    elif user_choice == "3":
        multiply()

    elif user_choice == "4":
        divide()

    else:
        print("\nInvalid option. Please choose a valid menu option.\n")