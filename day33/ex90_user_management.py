# User Management System (CLI)

# List to store all users
users = []

# Next unique ID for new users
next_id = 1

# Function to add a new user
def add_user(users):
    global next_id

    name = get_name()  # Get validated name input
    age = get_age()    # Get validated age input

    # Create a dictionary for the user
    user = {
        "id": next_id,
        "name": name,
        "age": age
    }

    next_id += 1        # Increment ID for next user
    users.append(user)  # Add user to the main list

    print(f"\n User '{name}' added successfully!\n")

# Function to get user's name
def get_name():
    
    while True:
        name = input("Enter user's name: ").strip()
        if name:
            return name.title()  # Capitalize first letters
        print(" Name cannot be empty. Please try again.")

# Function to get user's age
def get_age():

    while True:
        try:
            age = int(input("Enter user's age: "))
            if age < 0:
                print(" Age cannot be negative. Try again.")
                continue
            return age
        except ValueError:
            print(" Please enter a valid number.")

# Function to display all users
def show_users(users):
   
    print("\n--- All Registered Users ---\n")

    if not users:
        print("No users found.\n")
        return

    for user in users:
        print(f"[{user['id']}] Name: {user['name']} | Age: {user['age']}")

    show_statistics(users)  # Display user statistics

# Function to filter only adult users
def only_adults(users):
   return [user for user in users if user['age'] >= 18]

# Function to display adult users
def show_adults(users):
   
    adults = only_adults(users)

    print("\n--- Adult Users (18+) ---\n")

    if not adults:
        print("No adult users found.\n")
        return

    for user in adults:
        print(f"[{user['id']}] Name: {user['name']} | Age: {user['age']}")

# Function to show user statistics
def show_statistics(users):
  
    total = len(users)
    adults = len(only_adults(users))
    minors = total - adults

    print(f"\n📊 Statistics: Total Users: {total} | Adults: {adults} | Minors: {minors}\n")

# Function to display menu
def menu():
   
    print("\n=== User Management Menu ===")
    print("1 - Add a new user")
    print("2 - Show all users")
    print("3 - Show only adults")
    print("4 - Exit\n")

    try:
        return int(input("Choose an option (1-4): "))
    except ValueError:
        print(" Invalid input. Please enter a number between 1 and 4.")

# Mapping menu options to functions
options = {
    1: add_user,
    2: show_users,
    3: show_adults
}

# Main CLI loop
while True:
    
    option = menu()  # Show menu and get choice

    if option == 4:
        print("\n Goodbye! Thank you for using the system.\n")
        break
    elif option in options:
        options[option](users)  # Call the selected function
    else:
        print(" Invalid option. Please choose a number from 1 to 4.")