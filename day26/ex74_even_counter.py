# List of numbers
numbers = [1, 2, 3, 4, 5, 6]


# Function to count even numbers in a list
def count_even(numbers):
    count = 0

    # Loop through each number
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            count += 1

    return count


# Calculate result
result = count_even(numbers)

# Display result
print("\n=== EVEN NUMBER COUNTER ===")
print(f"Numbers: {numbers}")
print(f"Total even numbers: {result}")