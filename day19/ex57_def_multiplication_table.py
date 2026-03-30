
# Ask the user to choose a number
number = int(input("Enter a number: "))


# Function to display the multiplication table of a number
def multiplication_table(number):

    # Print a blank line for better CLI spacing
    print()

    # Display the table header
    print(f"======= MULTIPLICATION TABLE FOR {number} =======")

    # Loop from 1 to 10
    for i in range(1, 11):

        # Calculate the product
        product = i * number

        # Display the multiplication result
        print(f"{i} x {number} = {product}")


# Call the function
multiplication_table(number)