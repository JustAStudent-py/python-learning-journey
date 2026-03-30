# Function that calculates the sum from 1 up to the given number
def sum_numbers(number):
    total = 0

    # Loop through numbers from 1 to the chosen number
    for i in range(1, number + 1):
        total += i
        
    return total


# Ask the user for a number
number = int(input("Enter a number to calculate the sum from 1 to that number: "))

# Calculate the result
result = sum_numbers(number)

# Display the result
print(f"\nThe sum from 1 to {number} is: {result}")