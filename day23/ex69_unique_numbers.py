# Function that returns numbers that appear only once in the list
def unique_numbers(numbers):
    result = []

    # Loop through each number in the list
    for num in numbers:
        count = 0

        # Count how many times the number appears
        for n in numbers:
            if num == n:
                count += 1

        # If it appears only once, add to result
        if count == 1:
            result.append(num)

    return result


# CLI input
user_input = input("Enter numbers separated by space: ")

# Convert input string into a list of integers
numbers = list(map(int, user_input.split()))

# Get unique numbers
result = unique_numbers(numbers)

# Output result
print(f"\nNumbers that appear only once: {result}")