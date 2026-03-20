# List of numbers
numbers = [1, 2, 3, 4, 5, 6]


# Function to count odd numbers
def count_odd(numbers):
    count = 0

    # Loop through each number
    for num in numbers:
        # Check if the number is odd
        if num % 2 != 0:
            count += 1

    return count


# Calculate result
result = count_odd(numbers)

# Display result
print("\n=== ODD NUMBER COUNTER ===")
print(f"Numbers: {numbers}")
print(f"Total odd numbers: {result}")