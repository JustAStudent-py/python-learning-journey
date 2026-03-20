# List of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]


# Function to calculate the sum of a list
def sum_numbers(numbers):
    total = 0

    # Loop through each number in the list
    for num in numbers:
        total += num

    return total


# Calculate result
result = sum_numbers(numbers)

# Display result
print("\n=== SUM CALCULATOR ===")
print(f"Numbers: {numbers}")
print(f"Total sum: {result}")