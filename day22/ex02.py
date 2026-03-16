# Lists to store numbers and classifications
numbers = []
even_numbers = []
odd_numbers = []
unique_numbers = []

while True:
    try:
        # Ask the user to enter a number
        number = float(input("Enter a number (0 to exit): "))
    except ValueError:
        print("Please enter a valid number.")
        continue  # Return to the beginning of the loop

    # Exit condition
    if number == 0:
        print("Goodbye!")
        break

    # Store the number
    numbers.append(number)

    # Classify as even or odd
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

    # Build the list of unique numbers
    for n in numbers:
        if n not in unique_numbers:
            unique_numbers.append(n)


# Show statistics only if numbers were entered
if numbers:
    average = sum(numbers) / len(numbers)

    print("\n===== RESULTS =====")
    print(f"Total numbers entered: {len(numbers)}")
    print(f"Largest number: {max(numbers)}")
    print(f"Smallest number: {min(numbers)}")
    print(f"Average: {average:.2f}")
    print(f"Original list: {numbers}")
    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Unique numbers: {unique_numbers}")
else:
    print("No numbers were entered.")