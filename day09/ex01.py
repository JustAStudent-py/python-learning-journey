# Iterate from 1 to 29
for number in range(1, 30):

    # Check if the number is even
    if number % 2 == 0:
        print("Even")

    # If not even, check if it is odd and divisible by 5
    elif number % 5 == 0:
        print("Odd and multiple of 5")

    # If none of the conditions above apply,
    # the number is simply odd
    else:
        print("Odd")