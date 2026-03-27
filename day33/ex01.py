
# Function to add a new user
def add_user(users):
    name = input("Insert the name: ").title()
    age = int(input("Insert the age: "))

    user = {
        "name": name,
        "age": age
    }

    users.append(user)


# Function to display users
def show_users(users):
    print("\nUsers registered:")

    if not users:
        print("No users found.")
        return

    for user in users:
        print(f"Name: {user['name']} | Age: {user['age']}")


# Function to return only adult users
def only_adults(users):
    return [user for user in users if user['age'] >= 18]


# Function to display adult users
def show_adults(users):
    adults = only_adults(users)

    print("\nAdult users:")

    if not adults:
        print("No adults found.")
        return

    for user in adults:
        print(f"Name: {user['name']} | Age: {user['age']}")


# Main system
users = []

while True:
    print("\n--- MENU ---")
    print("1 - Add user")
    print("2 - Show all users")
    print("3 - Show only adults")
    print("4 - Exit")

    try:
        option = int(input("Choose an option: "))

        if option == 1:
            add_user(users)

        elif option == 2:
            show_users(users)

        elif option == 3:
            show_adults(users)

        elif option == 4:
            print("Goodbye.")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")