numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def analyze_numbers(numbers):
    # Lists to store even and odd numbers
    even_numbers = []
    odd_numbers = []
    
    # Variable to store the total sum of all numbers
    total = 0
    
    # Loop through each number in the list
    for n in numbers:
        # Add current number to total sum
        total += n
        
        # Check if the number is even
        if n % 2 == 0:
            even_numbers.append(n)
        else:
            # If not even, it is odd
            odd_numbers.append(n)
    
    # Return results organized in a dictionary
    return {
        "total_even": len(even_numbers),   # Total count of even numbers
        "total_odd": len(odd_numbers),    # Total count of odd numbers
        "even": even_numbers,             # List of even numbers
        "odd": odd_numbers,               # List of odd numbers
        "total": total                   # Sum of all numbers
    }

# Call the function and print the result
print(analyze_numbers(numbers))