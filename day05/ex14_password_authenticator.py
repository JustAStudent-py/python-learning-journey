# Password Checker

# Correct password stored in the system
correctPassword = "JustAStudent-py"   

# Variable to store the user input
userPassword = ""

# Loop runs until the user enters the correct password
while userPassword != correctPassword:
    
   
    userPassword = input("Enter your password: ")
    
    # Check if the password is correct
    if userPassword == correctPassword:
        print("Access Granted")
    
    # If the password is incorrect
    else:
        print("Access Denied")