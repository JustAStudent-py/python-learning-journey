# Ask the user to enter two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))


# Function to calculate and display the sum of the numbers
def sum_numbers():

    # Calculate the total
    total = number1 + number2

    # Display the result
    print(f"\nThe sum of the numbers is: {total}\n")


# Call the function
sum_numbers()