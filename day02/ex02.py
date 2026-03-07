# Number Comparison

try:
    number1 = float(input("Choose the first number: "))
    number2 = float(input("Choose the second number: "))

    #compare the numbers
    if number1 > number2:
        print(f"The number {number1} is bigger than {number2}")
        
    elif number1 == number2:
        print("Both numbers are equal")
    
    else:
        print(f"The number {number1} is less than {number2}")
        
#Handle invalid input
except ValueError:
    print("Error: Please choose a real number.")