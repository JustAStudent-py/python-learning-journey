# Function to convert a number to different bases
def convert_number(number):
    # Convert number to binary, octal and hexadecimal
    return {
        "bin": bin(number)[2:],
        "oct": oct(number)[2:],
        "hex": hex(number)[2:]
    }


# CLI menu loop
while True:
    print("\nChoose an option:")
    print("1 - Binary")
    print("2 - Octal")
    print("3 - Hexadecimal")
    print("4 - Exit")

    try:
        option_menu = int(input("Choose an option: "))

        # Exit condition
        if option_menu == 4:
            print("Goodbye.")
            break

        # Ask number only if needed
        number = int(input("Choose a number: "))

        # Call function and store result
        result = convert_number(number)

        # Display based on user choice
        if option_menu == 1:
            print(f"Binary: {result['bin']}")
        elif option_menu == 2:
            print(f"Octal: {result['oct']}")
        elif option_menu == 3:
            print(f"Hexadecimal: {result['hex']}")
        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter valid numbers.")