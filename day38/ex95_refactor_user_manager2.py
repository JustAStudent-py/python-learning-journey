# ==============================
# INPUT HELPERS
# ==============================

def get_name_and_email():
    """
    Captures user name and email input.
    Applies basic normalization to avoid inconsistencies.
    """
    print("\n=== USER INPUT ===")

    name = input("Enter user name: ").lower().strip()
    email = input("Enter user email: ").lower().strip()

    return name, email    


def is_valid_email(email):
    """
    Simple email validation.
    """
    return "@" in email and "." in email


# ==============================
# USER OPERATIONS
# ==============================

def create_user(users):
    """
    Creates a new user and stores it in the list.
    """
    print("\n=== CREATE USER ===")

    name, email = get_name_and_email()
    
    if not name:
        print("Invalid name.")
        return
    
    if not is_valid_email(email):
        print("Invalid email.")
        return
    
    user = {
        'id': len(users) + 1,
        'name': name,
        'email': email
    }
    
    users.append(user)

    print("User created successfully.")


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
    Removes a user by ID.
    """
    print("\n=== DELETE USER ===")

    found = False
    
    try:
        user_id = int(input("Enter user ID to remove: "))
    except ValueError:
        print("Invalid ID.")
        return
    
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            print("User removed successfully.")
            found = True
            break
    
    if not found:
        print("User not found.")      


def search_user_on_list(users):
    """
    Searches for a user by name.
    """
    print("\n=== SEARCH USER ===")
    
    if not users:
        print("No users found.")
        return
    
    found = False
    find_user = input("Enter a name to search: ").lower().strip()
    
    for user in users:
        if user['name'] == find_user:
            print("\nUser found:")
            print(f"[{user['id']}] Name: {user['name']} | Email: {user['email']}")
            found = True
        
    if not found:
        print("User not found.")


def update_user_email(users):
    """
    Updates the email of an existing user.
    """
    print("\n=== UPDATE EMAIL ===")

    name, email = get_name_and_email()
    found = False

    if not name:
        print("Invalid name.")
        return
    
    if not is_valid_email(email):
        print("Invalid email.")
        return

    # Check if email is already in use
    for u in users:
        if u['email'] == email:
            print("Email already in use.")
            return
    
    for user in users:
        if user['name'] == name:
            user['email'] = email
            found = True
    
    if found:
        print("Email updated successfully.")
    else:
        print("User not found.")


# ==============================
# SYSTEM CORE
# ==============================

users = []


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


def handle_options(option):
    """
    Executes the selected option.
    """
    if option in options:
        options[option](users)
    else:
        print("Invalid option. Please choose between 1 and 6.")


# Option mapping
options = {
    1: create_user,
    2: show_users,
    3: search_user_on_list,
    4: update_user_email,
    5: delete_user
}


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
        
        handle_options(option)
    
    except ValueError: 
        print("Invalid input. Please enter a number between 1 and 6.")