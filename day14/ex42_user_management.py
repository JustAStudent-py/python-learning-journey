# Variable to store the menu option
menu_choice = ""

# List that will store all users
users = []

while True:

    print("\n" + "=" * 35)
    print("        USER MANAGEMENT SYSTEM")
    print("=" * 35)
    print("[1] Add user")
    print("[2] List users")
    print("[3] Exit")
    print("=" * 35)

    menu_choice = input("Choose an option: ")

    # Exit program
    if menu_choice == "3":
        print("\nExiting program... Goodbye!")
        break

    # Add new user
    elif menu_choice == "1":

        print("\n--- Add New User ---")

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")

        # Create a dictionary for the user
        user = {
            "name": name,
            "age": age,
            "email": email
        }

        # Add user to the list
        users.append(user)

        print("\nUser successfully registered!")

    # List all users
    elif menu_choice == "2":

        print("\n--- Registered Users ---")

        if len(users) == 0:
            print("No users registered yet.")

        else:
            for index, user in enumerate(users, start=1):
                print("-" * 30)
                print(f"User #{index}")
                print(f"Name : {user['name']}")
                print(f"Age  : {user['age']}")
                print(f"Email: {user['email']}")

            print("-" * 30)

    else:
        print("\nInvalid option. Please choose a valid menu number.")