# Variable that stores the sum of all grades
total = 0

# Define how many grades will be entered
number_of_grades = 4

# Loop to collect each grade from the user
for i in range(1, number_of_grades + 1):
    
    # Convert user input to float to allow decimal grades
    grade = float(input(f"Insert your grade {i}: "))
    
    # Add each grade to the total sum
    total += grade

# Calculate the average grade
average = total / number_of_grades

# Display the average formatted to 2 decimal places
print(f"\nYour average is {average:.2f}")

# Determine student's status based on the average
if average >= 7:
    print("Status: Approved")
elif average >= 5:
    print("Status: Recovery")
else:
    print("Status: Failed")