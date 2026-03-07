# Login System with Limited Attempts

# The correct password stored in the system
correct_password = "JustAStudent-py"

# Variable to store the user's input
user_password = ""

# Maximum number of allowed attempts
max_attempts = 3

# Counter to track how many incorrect attempts were made
user_attempts = 0


# Loop that allows the user to try entering the password up to max_attempts times
for i in range(0, max_attempts):

    # Ask the user to enter the password
    user_password = input("Enter your password: ")

    # Check if the password is correct
    if user_password == correct_password:
        
        # Grant access if the password matches
        print("Access Granted.")
        print("Welcome!!!")
        
        # Stop the loop immediately since login was successful
        break


    # If the password is incorrect
    if user_password != correct_password:
        
        # Increase the failed attempts counter
        user_attempts += 1
        
        # Inform the user that the password is incorrect
        print("Incorrect password.")
        
        # Check if the user reached the maximum number of attempts
        if user_attempts == max_attempts:
            
            # Block the account after too many failed attempts
            print("Account blocked.")