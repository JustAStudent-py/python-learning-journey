# Ask the user to choose a number
number = int(input("Enter a number: "))

# Counters
even_count = 0
odd_count = 0
multiple_of_five = 0

print("\n=== Number Analysis ===\n")

# Loop through numbers from 1 to the chosen number
for i in range(1, number + 1):

    # Check if the number is even or odd
    if i % 2 == 0:
        even_count += 1
        print(f"Even number: {i}")
    else:
        odd_count += 1
        print(f"Odd number: {i}")

    # Check if the number is a multiple of five
    if i % 5 == 0:
        multiple_of_five += 1


# Display the results
print("\n======= SUMMARY =======")
print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")
print(f"Multiples of five: {multiple_of_five}")
