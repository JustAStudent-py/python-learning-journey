def verify_numbers(numbers):
    # Check if the list is empty to avoid errors
    if not numbers:
        return None

    # Create a copy of the list to avoid modifying the original
    sorted_numbers = sorted(numbers)

    # Variable to store the sum of all numbers
    total = 0

    # Loop through the list to calculate the sum
    for n in sorted_numbers:
        total += n

    # Calculate the average
    average = total / len(sorted_numbers)

    # Return the results in a dictionary
    return {
        "max": sorted_numbers[-1],   # Largest number
        "min": sorted_numbers[0],    # Smallest number
        "average": average          # Average value
    }


numbers = [10, 5, 20, 8, 15]

print(verify_numbers(numbers))