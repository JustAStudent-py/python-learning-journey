# Correct password (stored in system)
correct_password = "JustAStudent-py-2k26"


# Check if password contains at least one number
def has_number(password):
    return any(char.isdigit() for char in password)


# Check if password contains at least one uppercase letter
def has_uppercase(password):
    return any(char.isupper() for char in password)


# Check minimum password length
def has_min_length(password):
    return len(password) >= 8


# Check if password matches the correct one
def is_correct_password(password, correct_password):
    return password == correct_password


print("\n=== AUTHENTICATION SYSTEM ===\n")


while True:
    password = input("Enter your password: ")

    # Validation checks
    if not has_min_length(password):
        print("❌ Password must have at least 8 characters.\n")
        continue

    if not has_number(password):
        print("❌ Password must contain at least one number.\n")
        continue

    if not has_uppercase(password):
        print("❌ Password must contain at least one uppercase letter.\n")
        continue

    # Final verification
    if is_correct_password(password, correct_password):
        print("\n✅ Access granted. Welcome!")
        break
    else:
        print("❌ Access denied. Try again.\n")