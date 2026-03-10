# Dictionary containing students and their grades
students = {
    "Alice": 8.5,
    "Bob": 6.0,
    "Charlie": 9.2,
    "David": 5.5
}

# Print a header message
print("Approved students:")

# Iterate through the dictionary items (name and grade)
for name, grade in students.items():

    # Check if the student's grade is greater than or equal to 7
    if grade >= 7:
        
        # Print the name of the approved student
        print(name)