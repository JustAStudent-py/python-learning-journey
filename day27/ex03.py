# Function to return numbers divisible by 3 or 5
def divisible_numbers(n):
    result = []

    # Loop from 1 to n
    for num in range(1, n + 1):

        # Check if divisible by 3 or 5
        if num % 3 == 0 or num % 5 == 0:
            result.append(num)

    return result


# User input
try:
    number = int(input("Enter a number to find multiples of 3 or 5: "))

    if number < 1:
        print("Please enter a positive number.")
    else:
        result = divisible_numbers(number)

        print("\n=== RESULT ===")
        print(f"Numbers divisible by 3 or 5 (1 to {number}):")
        print(result)

except ValueError:
    print("Please enter a valid integer.")