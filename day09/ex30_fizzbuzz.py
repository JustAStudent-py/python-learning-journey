# Iterate from 1 to 20 (inclusive)
for number in range(1, 21):

    # Check the most specific condition first:
    # divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # Divisible only by 3
    elif number % 3 == 0:
        print("Fizz")

    # Divisible only by 5
    elif number % 5 == 0:
        print("Buzz")

    # If none of the conditions above are met,
    # print the number itself
    else:
        print(number)