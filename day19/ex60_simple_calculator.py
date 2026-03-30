
# Define mathematical operation functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# Dictionary that maps operation names to their functions
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}


# Display available operations to the user
print("\n=== Simple CLI Calculator ===")
print("Available operations:")
print("- add")
print("- subtract")
print("- multiply")
print("- divide\n")


# Ask the user to choose an operation
choice = input("Choose an operation: ").lower()

# Ask the user for the numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))


# Execute the selected operation
result = operations[choice](a, b)

# Display the result
print(f"\nResult: {result}\n")

