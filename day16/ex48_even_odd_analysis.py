# List of numbers to analyze
numbers = [2, 5, 8, 11, 14, 17]

# Counters for even and odd numbers
even_count = 0
odd_count = 0

# Variable to store the sum of even numbers
even_sum = 0

# Iterate through each number in the list
for number in numbers:
    
    # Check if the number is even
    if number % 2 == 0:
        
        # Add the number to the sum of even numbers
        even_sum += number
        
        # Increase the even number counter
        even_count += 1
    
    else:
        # Increase the odd number counter
        odd_count += 1

# Print the results
print(f"Even Numbers: {even_count}")
print(f"Odd numbers: {odd_count}")   
print(f"Even sum: {even_sum}")