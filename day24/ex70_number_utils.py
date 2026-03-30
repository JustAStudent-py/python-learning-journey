# Function to check if a number is even or odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# Function to split a number into digits in reverse order
def digitize(n):
    result = []

    for d in str(n):
        result.append(int(d))  # convert the current digit, not the whole number

    result.reverse()  # reverse the list
    return result


# Example usage
print(even_or_odd(7))       # Output: Odd
print(even_or_odd(12))      # Output: Even
print(digitize(348))        # Output: [8, 4, 3]