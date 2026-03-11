# Lists to store numbers
numbers = []
even_numbers = []
odd_numbers = []



# Loop to continuously ask the user for numbers
while True:
    
    # Ask the user to input a number
    # Entering 0 will stop the program
    number = int(input("Choose a number (0 to exit): "))
    
    # Exit condition
    if number == 0:
        break

    # Add the number to the main list
    numbers.append(number)
    
    # Check if the number is even or odd
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Check if the user entered any numbers
if numbers:    
    
    # Calculate total and average
    total = sum(numbers)
    average = total / len(numbers)

    # Sort numbers in ascending order
    numbers.sort()

    print("\n" + "=" * 20)
    
    # Show results
    print(f"All numbers: {numbers}")
    
    print(f"Average: {average:.2f}")
    
    print(f"Total: {total}")
    
    # Access highest and lowest numbers
    print(f"Highest number: {numbers[-1]}")
    
    print(f"Lowest number: {numbers[0]}")
    
    # Show even and odd numbers
    print(f"Even numbers: {even_numbers}")
    
    print(f"Odd numbers: {odd_numbers}")

else:
    # Message if no numbers were entered
    print("No numbers entered")