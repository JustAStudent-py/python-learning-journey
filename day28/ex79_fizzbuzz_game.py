# FizzBuzz Program
# This program prints numbers from 1 to N
# replacing multiples of 3 with "Fizz",
# multiples of 5 with "Buzz",
# and multiples of both with "FizzBuzz"

def fizzbuzz(number):
    result = []  # List to store the results

    # Loop through numbers from 1 to the chosen number
    for count in range(1, number + 1):

        # Check if divisible by BOTH 3 and 5 first
        if count % 3 == 0 and count % 5 == 0:
            result.append("FizzBuzz")

        # Check if divisible only by 5
        elif count % 5 == 0:
            result.append("Buzz")

        # Check if divisible only by 3
        elif count % 3 == 0:
            result.append("Fizz")

        # If none of the conditions above, keep the number
        else:
            result.append(count)

    return result


# -------- CLI (User Interface) --------

print("=" * 40)
print(" Welcome to FizzBuzz Program ")
print("=" * 40)

try:
    number = int(input(" Choose a positive number: "))

    if number <= 0:
        print(" Please enter a number greater than 0.")

    else:
        print("\n Processing...\n")

        result = fizzbuzz(number)

        print(" Result:\n")
        print(result)

except ValueError:
    print(" Invalid input! Please enter a valid integer.")