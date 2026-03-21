# Function to calculate the sum from 1 up to n
def sum_numbers(n):
    total = 0

    # Loop from 1 to n
    for i in range(1, n + 1):
        total += i

    return total


# Ask user for input
try:
    number = int(input("Enter a number to calculate the sum from 1 to n: "))

    if number < 1:
        print("Please enter a positive number.")
    else:
        result = sum_numbers(number)

        print("\n=== RESULT ===")
        print(f"Sum from 1 to {number}: {result}")

except ValueError:
    print("Please enter a valid integer.")