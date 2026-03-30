# Function to analyze numbers from 1 to n
def analyze_numbers(n):
    even_count = 0
    odd_count = 0
    total_sum = 0

    # Loop from 1 to n
    for num in range(1, n + 1):
        total_sum += num

        # Check if number is even or odd
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count, total_sum


# User input
try:
    number = int(input("Enter a number to analyze from 1 to n: "))

    if number < 1:
        print("Please enter a positive number.")
    else:
        even, odd, total = analyze_numbers(number)

        print("\n=== ANALYSIS RESULT ===")
        print(f"Range analyzed: 1 to {number}")
        print(f"Even numbers: {even}")
        print(f"Odd numbers: {odd}")
        print(f"Total sum: {total}")

except ValueError:
    print("Please enter a valid integer.")