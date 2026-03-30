# Password validator

while True:

    # Ask the user to input a password
    user_password = input("Insert your password: ")

    # Check if the password contains at least one digit
    has_number = any(char.isdigit() for char in user_password)

    # Check if the password contains at least one letter
    has_letter = any(char.isalpha() for char in user_password)

    # Validate password rules:
    # - Minimum length of 8 characters
    # - At least one number
    # - At least one letter
    if len(user_password) >= 8 and has_number and has_letter:
        print(f"Your password '{user_password}' is valid.")
        break

    else:
        # If the password does not meet the requirements, ask again
        print("The password does not meet the requirements.")