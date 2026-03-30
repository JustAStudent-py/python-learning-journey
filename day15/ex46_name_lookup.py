# List of available names
names = ["Elias", "Igor", "Andre", "Marcelinho", "Vitoria"]

# Loop until the user enters a valid name
while True:

    # Ask the user for a name
    # .capitalize() ensures the first letter is uppercase
    name = input("Choose a name: ").capitalize()

    # Check if the name exists in the list
    if name in names:
        print(f"This name: {name} is on the list.")
        break  # Exit the loop if the name is found
    else:
        print("Name not found, try again.")