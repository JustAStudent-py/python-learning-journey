# Initial account balance
balance = 0

# List to store transaction history
history = []

def show_balance(balance, history):  # Displays the current user balance
    
    if balance == 0:
        print("Current balance: $0.00")
    else:
        print(f"Balance: ${balance:.2f}")
    
    return balance, history


def deposit_value(balance, history):  # Allows the user to deposit money
    
    try:
        # Ask for deposit amount
        deposit_amount = float(input("Enter the amount to deposit: $"))
    except ValueError:
        print("Please enter a valid number.")
        return balance, history

    # Check if the amount is positive
    if deposit_amount > 0:
        balance += deposit_amount
        history.append(f"Deposit: ${deposit_amount:.2f}")
        print(f"Deposit: ${deposit_amount:.2f} | New balance: ${balance:.2f}")
    else:
        print("Deposit amount must be greater than zero.")
    
    return balance, history


def withdraw_balance(balance, history):  # Allows the user to withdraw money
    
    # Check if there is available balance
    if balance <= 0:
        print("No balance available.")
        return balance, history

    try:
        # Ask for withdrawal amount
        withdraw_amount = float(input("Enter the amount to withdraw: $"))
    except ValueError:
        print("Please enter a valid number.")
        return balance, history

    # Check if withdrawal exceeds balance
    if withdraw_amount > balance:
        print("Withdrawal amount exceeds available balance.")
    else:
        balance -= withdraw_amount
        history.append(f"Withdrawal: ${withdraw_amount:.2f}")
        print(f"Withdrawal: ${withdraw_amount:.2f} | New balance: ${balance:.2f}")
    
    return balance, history    


def show_history(balance, history):  # Function to display history
    
    # Check if history list is empty
    if not history:
        print("No transactions have been made yet.")
    
    else:
        print("\n=== TRANSACTION HISTORY ===")
        for item in history:
            print(item)
    
    return balance, history


def menu():  # Displays the main menu and returns user choice
    
    print("=" * 40)
    print("ATM System")
    print("=" * 40)
    print("1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Show History")
    print("5 - Exit")
    print("=" * 40)

    # Validate user input
    try:
        return int(input("Choose an option (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return 0


# Mapping options to functions
options = {
    1: show_balance,
    2: deposit_value,
    3: withdraw_balance,
    4: show_history
}


# Main system loop
while True:
    option = menu()

    if option == 5:
        print("Thank you for using the system.")
        break
    elif option in options:
        balance, history = options[option](balance, history)
    else:
        print("Invalid option. Please choose a number between 1 and 5.")