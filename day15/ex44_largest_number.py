# Create an empty list to store the numbers
numbers = []

# Ask the user to enter 5 numbers
for i in range(1, 6):

    # Convert the input to an integer
    number = int(input("Choose a number: "))

    # Add the number to the list
    numbers.append(number)

# Sort the list in ascending order
numbers.sort()

# The largest number will be the last element in the sorted list
print(f"Largest number: {numbers[-1]}")