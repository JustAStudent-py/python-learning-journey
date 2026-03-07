# Even Numbers Sum Program

# Variable to store the total sum
total = 0

# Loop from 1 to 100
for i in range(1, 101):

    # Check if the number is even
    # Even numbers have remainder 0 when divided by 2
    if i % 2 == 0:

        # Add the even number to the total
        total += i 

        # Print the current total after addition
        print(total)
