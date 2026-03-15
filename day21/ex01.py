# List to store users
users = []


# Function to display the menu
def menu():
    print("\n" + "=" * 40)
    print("1 - Add User")
    print("2 - Search User")
    print("3 - List Users")
    print("4 - Remove User")
    print("5 - Exit")
    print("=" * 40)


# Function to add a new user
def add_user():
    name = input("Enter the user's name: ").title()
    age = int(input("Enter the user's age: "))
    email = input("Enter the user's email: ").lower()

    user = {
        "name": name,
        "age": age,
        "email": email
    }

    users.append(user)

    print("User registered successfully.")


# Function to search for a user
def search_user():
    user_choice = input("Enter the name to search: ").title()

    for user in users:
        if user["name"] == user_choice:
            print(f"Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")
            return

    print("User not found.")


# Function to list all users
def list_users():
    if users:
        print("\n=== Registered Users ===")
        for user in users:
            print(f"Name: {user['name']} | Age: {user['age']} | Email: {user['email']}")
    else:
        print("No users registered.")


# Function to remove a user
def remove_user():
    remove_choice = input("Enter the name of the user to remove: ").title()

    for user in users:
        if user["name"] == remove_choice:
            users.remove(user)
            print("User removed successfully.")
            return

    print("User not found.")


# Main program loop
while True:

    menu()

    option_menu = input("Choose an option: ")

    if option_menu == "5":
        print("Goodbye.")
        break

    elif option_menu == "1":
        add_user()

    elif option_menu == "2":
        search_user()

    elif option_menu == "3":
        list_users()

    elif option_menu == "4":
        remove_user()

    else:
        print("Please choose a valid option.")