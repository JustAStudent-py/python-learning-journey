# Function that calculates the sum from 1 up to the given number
def sum_number(number):
    total = 0

    # Loop through numbers from 1 to the given number
    for i in range(1, number + 1):
        total += i
    
    return total


# Function that returns the square of a number
def square_number(number):
    return number ** 2


# Function that multiplies a number by two
def multiply_by_two(number):
    return number * 2


# Function that checks if a number is even
def check_number(number):
    return number % 2 == 0


print("\n=== Function Results ===\n")

print(f"Square of 5: {square_number(5)}")
print(f"8 multiplied by two: {multiply_by_two(8)}")
print(f"Sum from 1 to 8: {sum_number(8)}")

print(f"Is 5 even? {check_number(5)}")
print(f"Is 8 even? {check_number(8)}")
