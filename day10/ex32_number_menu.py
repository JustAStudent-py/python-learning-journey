import time
import os

# Store user's menu selection
menu_option = ""

# Detect correct clear command once (avoid repetition)
clear_command = "cls" if os.name == "nt" else "clear"

while True:

    print("-" * 30)
    print("1 - Count numbers")
    print("2 - Show even and odd numbers")
    print("3 - Show numbers divisible by 3")
    print("4 - Exit")
    print("-" * 30)

    menu_option = input("Choose an option: ")

    # OPTION 1 — COUNT NUMBERS
    if menu_option == "1":

        limit = int(input("Count until: "))
        print("Counting...")

        for number in range(1, limit + 1):
            time.sleep(1)
            print(number)

        time.sleep(3)
        os.system(clear_command)

    # OPTION 2 — EVEN OR ODD
    elif menu_option == "2":

        limit = int(input("Count until: "))
        print("Counting...")

        for number in range(1, limit + 1):
            time.sleep(1)

            if number % 2 == 0:
                print(f"Even number: {number}")
            else:
                print(f"Odd number: {number}")

        time.sleep(3)
        os.system(clear_command)

    # OPTION 3 — DIVISIBLE BY 3
    elif menu_option == "3":

        limit = int(input("Count until: "))
        print("Checking divisibility by 3...")

        for number in range(1, limit + 1):
            time.sleep(1)

            if number % 3 == 0:
                print(f"{number} is divisible by 3.")
            else:
                print(f"{number} is not divisible by 3.")

        time.sleep(3)
        os.system(clear_command)

    # OPTION 4 — EXIT
    elif menu_option == "4":
        print("Goodbye.")
        break

    # INVALID OPTION
    else:
        print("Invalid option. Please choose between 1 and 4.")
        time.sleep(2)
        os.system(clear_command)