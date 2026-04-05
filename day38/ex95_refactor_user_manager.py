users = []
emails = set()

def create_user(users):
    next_id = 1

    name = input("Insert the user name:  ").lower().strip()
    email = input("Insert the user email: ").lower()

    user = {
        "id": len(users),
        "name": name,
        "email": email
    }
    
    
    users.append(user)
    next_id += 1
    emails.add(email)
    
    return users

def list_users(users):

    if not users:
        print("Not users found")
        return users
    else:
        for user in users:
            print(f"[{user['id']}] Name: {user['name']} | Email: {user['email']}")
        return users

def find_user(users):


    if not users:
        print("No users registred")
        return 

    
    name = input("Insert the user name: ").lower().strip()
    
    for user in users:  
        if user["name"] == name:
            print("\nUser Found: ")
            print (f"ID:[{user['id']}] Name: {user['name']} | Email: {user['email']}")
            return users
        else:
            print("User Not Found")
    
    return users

def is_valid_email(users):
    print()
    
def remove_user(users):

    if not users:
        print("No users registred")
        return users
    
    list_users()

    name = input("Insert the users name of who want remove: ").lower().strip()

    for user in users:
        if user['name'] == name:
            users.remove(user)
            print("User removed with success")
            return users
        else:
            print("No user found.")
    return users
    
def update_email(users):

    if not users:
        print("No users email registred")
        return users
    
    list_users()

    name = input("Insert the user name who want update the email: ").lower().strip()

    for user in users:
        if user['name'] == name:
            new_email = input("insert the new email: ").lower()
            emails.remove(user['email'])
            emails.add(new_email)
            print("Nem email registred with success. ")
            return users

def menu():
    
    print("\n" + "=" * 40)
    print("        USER MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1 - Create user.")
    print("2 - Show users.")
    print("3 - Search user.")
    print("4 - Update Email.")
    print("5 - Remove user.")
    print("6 - Exit.")
    print("=" * 40)

    try:
        return int(input("Choose an option: beetween (1-6): "))
    except ValueError:
        return 0
    
def handle_option(option):
    
    if option in options:
        options[option](users)
    else:
        print("Please choose a valid option.")

options = {
    1: create_user,
    2: list_users,
    3: find_user,
    4: update_email,
    5: remove_user
}

while True:
    try:
        option = menu()

        if option == 6:
            print("Thank you for use the system.")
            break

        handle_option(option)
    except ValueError:
        print("Please choose a valid option beetween (1-6).")


