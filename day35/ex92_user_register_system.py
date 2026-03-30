import time

users = []
next_id = 1

def add_user():
    global next_id

    name = input("Insert the user name: ").title()
    
    try:
        email = input("Insert the email: ").lower()
        
        validate_email(email)
    except ValueError:
        print("Email invalid")



    age = int(input("Insert the age: "))
    
    user = {
        "id": next_id,
        "name": name,
        "email": email,
        "age": age
    }

    users.append(user)
    next_id += 1
    
    print("Wait.")
    time.sleep(1)
    print("Wait..")
    time.sleep(1)
    print("Wait...")
    time.sleep(1)
    print("User registred with success.")


def show_users():
    
    if not users:
        print("No users registred.")
        return
    
    print("Showing users")
    time.sleep(1)
    
    for user in users:
        print(f"[{user['id']}] User: {user['name']} | Age: {user['age']} | email: {user['email']}")
        
def remove_user():
    
    if not users:
        print("No users Registred.")
        return
    
    show_users()

    try:
        user_id = int(input("Choose the id of the user: "))
    except ValueError:
        print("Invalid ID")
        return

    for user in users:
        if user_id == user['id']:
            users.remove(user)
            print("User removed with success")
        
def menu():
    
    print("=" * 40)
    print("User register System")
    print("=" * 40)
    print("1- Add user")
    print("2- Show user")
    print("3- Remove user")
    print("4- Exit")
    print("=" * 40)

def validate_email(users):
    
    for arroba in user['email']:
        if not "@" in user['email']:
            print("Insert a valid email.")
            return
        
options = {
    1: add_user,
    2: show_users,
    3: remove_user
}

def handle_option(choice):
    
    if choice in options:
        options[choice]()
    else:
        print("Please choose a valid option. ")




while True:
    menu()
    
    try:
        choice = int(input("Choose an option: "))
        
        if choice == 4:
            print("Goodbye")
            break

        handle_option(choice)

    except ValueError:
        print("Enter a valid number. ")     