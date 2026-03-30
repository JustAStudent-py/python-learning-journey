# Custom FizzBuzz Program
# Allows the user to define which numbers will be "Fizz" and "Buzz"

def custom_fizzbuzz(limit, fizz_number, buzz_number):
    result = []

    # Loop from 1 to the chosen limit
    for count in range(1, limit + 1):

        # Check if divisible by both numbers
        if count % fizz_number == 0 and count % buzz_number == 0:
            result.append("FizzBuzz")

        # Check only Fizz condition
        elif count % fizz_number == 0:
            result.append("Fizz")

        # Check only Buzz condition
        elif count % buzz_number == 0:
            result.append("Buzz")

        # Otherwise, keep the number as string
        else:
            result.append(str(count))

    return result


# -------- CLI --------

print("=" * 40)
print("  Custom FizzBuzz")
print("=" * 40)

try:
    limit = int(input(" Choose the limit number: "))
    fizz_number = int(input(" Choose the Fizz number: "))
    buzz_number = int(input(" Choose the Buzz number: "))

    # Validation
    if limit <= 0 or fizz_number <= 0 or buzz_number <= 0:
        print(" All numbers must be greater than 0.")

    else:
        print("\n Processing...\n")

        result = custom_fizzbuzz(limit, fizz_number, buzz_number)

        print(" Result:\n")

        # Print line by line (more readable)
        for i, value in enumerate(result, start=1):
            print(f"{i} → {value}")

except ValueError:
    print(" Invalid input! Please enter only integers.")