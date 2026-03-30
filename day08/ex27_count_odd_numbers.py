# Counter for odd numbers
count = 0

# Iterate from 1 to 100
for number in range(1, 101):
    
    # Check if number is odd
    if number % 2 == 1:
        
        # Increment counter
        count += 1

# Display result
print(f"Total odd numbers: {count}")