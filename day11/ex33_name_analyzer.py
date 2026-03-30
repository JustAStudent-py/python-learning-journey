
# Infinite loop to keep the program running until the user decides to exit
while True:

    # Ask the user to insert their full name and remove extra spaces
    name = input("Insert your full name: ").strip()

    # Check if the user wants to exit the program
    if name.lower() == "exit":
        break

    # Print the name in uppercase
    print("Upper:", name.upper())

    # Print the name in lowercase
    print("Lower:", name.lower())

    # Count the total number of characters
    print("Letters:", len(name))

    # Count the number of words in the name
    print("Words:", len(name.split()))