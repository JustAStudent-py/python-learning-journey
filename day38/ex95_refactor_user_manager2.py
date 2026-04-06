# ==============================
# INPUT HELPERS
# ==============================

def get_name_and_email():
    """
    Captures user name and email input.
    Applies normalization to ensure consistency.
    """
    print("\n=== USER INPUT ===")

    name = input("Enter user name: ").lower().strip()
    email = input("Enter user email: ").lower().strip()

    return name, email    

def find_user(name, users):
    """
    Searches for a user by name.
    Returns the user object or None.
    """
    for user in users:
        if user['name'] == name:
            return user
    return None

def email_exists(email, users):
    """
    Checks if an email already exists in the system.
    """
    for user in users:
        if user['email'] == email:
            return True
    return False
    
def is_valid_email(email):
    """
    Simple email validation.
    """
    return "@" in email and "." in email

# ==============================
# BUSINESS LOGIC
# ==============================

def create_user_logic(name, email, users, next_id):
    """
    Handles user creation rules and validation.
    Returns either:
    - user dict (success)
    - error string (failure)
    """
    if not name:
        return "invalid_name"
    
    if not is_valid_email(email):
        return "invalid_email"
    
    if email_exists(email, users):
        return "email_exists"
    
    user = {
        "id": next_id,
        "name": name,
        "email": email
    }
    
    users.append(user)
    return user

def update_email_logic(users, name, new_email):
    """
    Handles email update rules.
    """
    user = find_user(name, users)
    
    if not user:
        return "not_found"
    
    if not is_valid_email(new_email):
        return "invalid_email"
    
    if email_exists(new_email, users):
        return "email_exists"
    
    user['email'] = new_email
    return "success"

def delete_user_logic(user_id, users):
    """
    Removes a user by ID.
    Returns True if removed, False otherwise.
    """
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return True
    return False

# ==============================
# CLI LAYER
# ==============================

def create_user(users, next_id):
    """
    CLI wrapper for user creation.
    """
    print("\n=== CREATE USER ===")

    name, email = get_name_and_email()
    
    result = create_user_logic(name, email, users, next_id)

    # Interprets logic response
    if result == "invalid_name":
        print("Invalid name.")
        return next_id
    
    elif result == "invalid_email":
        print("Invalid email.")
        return next_id
    
    elif result == "email_exists":
        print("Email already exists.")
        return next_id
    
    else:
        print("User created successfully.")
        return next_id + 1

def show_users(users):
    """
    Displays all registered users.
    """
    print("\n=== USER LIST ===")
    
    if users:
        for user in users:
            print(f"[{user['id']}] Name: {user['name']} | Email: {user['email']}")
        return users
    else:
        print("No users registered.")

def delete_user(users):
    """
    CLI wrapper for user deletion.
    """
    print("\n=== DELETE USER ===")

    try:
        user_id = int(input("Enter user ID to remove: "))
    except ValueError:
        print("Invalid ID.")
        return

    if delete_user_logic(user_id, users):
        print("User removed successfully.")
    else:
        print("User not found.")

def search_user_on_list(users):
    """
    CLI wrapper for user search.
    """
    print("\n=== SEARCH USER ===")
    
    if not users:
        print("No users found.")
        return
    
    name = input("Enter a name to search: ").strip()
    
    user = find_user(name, users)

    if user:
        print("\nUser found:")
        print(f"[{user['id']}] Name: {user['name']} | Email: {user['email']}")
    else:
        print("User not found.")

def update_user_email(users):
    """
    CLI wrapper for updating user email.
    """
    print("\n=== UPDATE EMAIL ===")

    name, new_email = get_name_and_email()
    
    result = update_email_logic(users, name, new_email)

    if result == "not_found":
        print("User not found.")
    elif result == "invalid_email":
        print("Invalid email.")
    elif result == "email_exists":
        print("Email already exists.")
    else:
        print("Email updated successfully.")

# ==============================
# SYSTEM CORE
# ==============================

users = []
next_id = 1

def menu():
    """
    Displays the main system menu.
    """
    print("\n" + "=" * 40)
    print("        USER MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1 - Create user")
    print("2 - Show users")
    print("3 - Search user")
    print("4 - Update email")
    print("5 - Remove user")
    print("6 - Exit")
    print("=" * 40)

# ==============================
# MAIN LOOP
# ==============================

while True:
    menu()
    
    try:
        option = int(input("Choose an option (1-6): "))

        if option == 6:
            print("\nClosing system. Goodbye.")
            break
        
        elif option == 1:
            next_id = create_user(users, next_id)
        elif option == 2:
            show_users(users)
        elif option == 3:
            search_user_on_list(users)
        elif option == 4:
            update_user_email(users)
        elif option == 5:
            delete_user(users)
        else:
            print("Invalid option. Please choose between 1 and 6.")
    
    except ValueError: 
        print("Invalid input. Please enter a number between 1 and 6.")