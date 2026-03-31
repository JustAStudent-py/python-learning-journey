# Initial account balance
balance = 0


def show_balance():
    """
    Displays the current account balance.
    """
    if balance == 0:
        print("No balance available.")
    else:
        print(f"Balance: ${balance:.2f}")


def deposit_amount():
    """
    Allows the user to deposit money into the account.
    """
    global balance

    try:
        # Ask user for deposit amount
        deposit_value = float(input("Enter the amount to deposit: $"))
    except ValueError:
        print("Please enter a valid number.")
        return 0

    # Check if value is positive
    if deposit_value > 0:
        balance += deposit_value
        print(f"Deposit: ${deposit_value:.2f} | New balance: ${balance:.2f}")
        return balance
    else:
        print("Deposit amount must be greater than zero.")


def withdraw_amount():
    """
    Allows the user to withdraw money from the account.
    """
    global balance

    # Check if there is available balance
    if balance <= 0:
        print("No balance available.")
        return

    try:
        # Ask user for withdrawal amount
        withdraw_value = float(input("Enter the amount to withdraw: $"))
    except ValueError:
        print("Please enter a valid number.")
        return 0

    # Check if withdrawal exceeds balance
    if withdraw_value > balance:
        print("Withdrawal amount exceeds available balance.")
    else:
        balance -= withdraw_value
        print(f"Withdrawal: ${withdraw_value:.2f} | New balance: ${balance:.2f}")
        return balance


def menu():
    """
    Displays the main menu and returns the selected option.
    """
    print("=" * 40)
    print("ATM System")
    print("=" * 40)
    print("1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")
    print("=" * 40)

    try:
        return int(input("Choose an option (1-4): "))
    except ValueError:
        print("Invalid input. Please choose a number between 1 and 4.")
        return 0


# Mapping options to functions
options = {
    1: show_balance,
    2: deposit_amount,
    3: withdraw_amount,
}


# Main system loop
while True:
    option = menu()

    if option == 4:
        print("Thank you for using the system.")
        break
    elif option in options:
        options[option]()  # Execute selected function
    else:
        print("Invalid option. Choose a number between 1 and 4.")