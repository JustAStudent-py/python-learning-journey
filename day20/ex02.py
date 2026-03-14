# List to store the numbers entered by the user
numbers = []

# Counters
even_count = 0
odd_count = 0


print("\n=== Number Statistics CLI ===")
print("Enter numbers to analyze them.")
print("Type 0 to exit.\n")

while True:
    # Ask the user to enter a number
    number = int(input("Enter a number (0 to exit): "))

    # Exit condition
    if number == 0:
        print("\nExiting program...\n")
        break
    

    # Store the number in the list
    numbers.append(number)

    # Check if the number is even or odd
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


# Sort the list of numbers
numbers.sort()

if numbers:
    # Display results
    print("======= RESULTS =======")
    print(f"Total numbers entered: {len(numbers)}")
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    
    print(f"Largest number: {numbers[-1]}")
    print(f"Smallest number: {numbers[0]}")
