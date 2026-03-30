# Countdown Program

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Loop from the chosen number down to 0
# start = number
# stop = -1 (not included, so 0 will be the last number printed)
# step = -1 (decreases by 1 each iteration)
for i in range(number, -1, -1):

    # Print the current value of the countdown
    print(i)