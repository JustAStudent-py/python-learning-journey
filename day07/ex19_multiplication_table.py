# Multiplication Table Program

# Ask the user to choose a number
user_number = int(input("Choose a number: "))

# Variable to store the result of multiplication
product = 0

# Display table title
print(f"======= MULTIPLICATION TABLE OF {user_number} =======")

# Loop from 1 to 10
for i in range(1, 11):

    # Calculate the multiplication
    product = i * user_number
   
    # Display the result
    print(f"{i} x {user_number} = {product}")