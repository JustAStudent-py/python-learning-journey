# Grade Average Calculator

try:
    grade1 = float(input("Write the first grade "))
    grade2 = float(input("Write the second grade "))
    grade3 = float(input("Write the third grade "))
    grade4 = float(input("Write the fourth grade "))

    # Calcutate the average of grades
    average = (grade1 + grade2 + grade3 + grade4) / 4
    
    print(f"The average is {average:.2f} points")

#Handle invalid input
except ValueError:
    print("Error: Please enter valid numeric grades.")