# Number Sign Classifier
try:
    number = float(input("Choose a number: "))

    # Check if the number is positive, negative, or zero
    if number > 0:
        print("Your number is positive")

    elif number < 0:
        print("Your number is negative")
    else:
        print("Your number is zero")

# Handle invalid input (not a number)    
except ValueError:
    print("Error: Please enter a valid real number.")