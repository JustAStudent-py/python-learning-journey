# Variable to store the total sum
sum = 0

# Loop that runs 10 times
for i in range(1, 11):

    # Ask the user for a number and convert it to float
    number = float(input("Choose a number: "))

    # Add the number to the total
    sum += number

average = sum / 10

# Print the final sum with two decimal places
print(f"The total sum is {sum:.2f}")
print(f"The average is: {average:.2f}")