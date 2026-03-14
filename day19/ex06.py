# Function to print a greeting message
def say_hello():
    print("Hello!")


# Function to print a Python message
def say_python():
    print("Say Python!")


# Function to print a goodbye message
def say_goodbye():
    print("Goodbye!")


# Dictionary that maps commands to functions
messages = {
    "hello": say_hello,
    "python": say_python,
    "bye": say_goodbye
}


#  main programming loop
while True:
# CLI header
    print("\n=== Message CLI ===")
    print("Available commands: hello, python, bye\n")


    # Ask the user to choose a command
    user_choice = input("Enter a command: ").lower()

    if user_choice == "bye":
        break

    # Execute the selected command
    messages[user_choice]()

    