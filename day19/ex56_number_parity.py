# Ask the user to enter a number
number = int(input("Enter a number: "))


# Function to check if the number is even or odd
def check_even(number):

    # Check if the number is divisible by 2
    if number % 2 == 0:
        print("\nResult: Even number\n")
    else:
        print("\nResult: Odd number\n")


# Call the function
check_even(number)