# List to store all available items (products)
items = []

# List to store items added to the cart
cart = []

# Variable to generate unique IDs for each item
next_id = 1


# Function to add a new item to the system
def add_items():
    global next_id  # allows modification of the global variable

    # Get item data from user
    name = input("What's is the product: ").lower()
    price = float(input("Insert the price of the product: $"))
    
    # Create item as a dictionary
    item = {
        "id": next_id,
        "name": name,
        "price": price    
    }
    
    # Add item to the items list
    items.append(item)

    # Increment ID for next item
    next_id += 1

    print("Item cadastred.")


# Function to display all registered items
def show_items():
    
    print("\n Products :")

    # Check if there are no items
    if not items:
        print("No items found: ")
        return
    
    # Loop through all items and display them
    for item in items:
        print(f"[{item['id']} Product: {item['name']} | Price: ${item['price']}")


# Function to create a cart by selecting items
def create_cart():
    
    # Show available items before selecting
    show_items()

    # If no items exist, stop execution
    if not items:
        print("No items registred")
        return
    
    # Loop to allow multiple selections
    while True:
        
        try:
            # Ask user to choose item by ID
            id_item = int(input("Choose the id of the itens (0 to stop)"))
        except ValueError:
            print("Invalid id")
            return
        
        # Stop adding items if user enters 0
        if id_item == 0:
            break
        
        # Search for the item with the chosen ID
        for item in items:
            if item['id'] == id_item:
                # Add item to cart
                cart.append(item)
            else:
                # This message will appear multiple times (logic detail)
                print("No item found")
            


# Function to display items in the cart
def show_cart():
    
    # Check if cart is empty
    if not cart:
        print("No cart created")
        return

    # Loop through cart items and display them
    for item in cart:
        print(f"[{item['id']}] | Name: {item['name']} | Price: {item['price']}")


# Placeholder function (not implemented yet)
def delete_items():
    print()


# Function to display menu options
def menu():
    print("=" * 40)
    print("CLI Eletronic box")
    print("=" * 40)
    print("1- Add items.")
    print("2- Create cart .")
    print("3- Show Cart.")
    print("4- Exit.")


# Dictionary mapping menu options to functions
options = {
    1: add_items,
    2: create_cart,
    3: show_cart
}


# Function to handle user's choice
def handle_option():

    # Check if the choice exists in options dictionary
    if choice in options:
        # Execute the corresponding function
        options[choice]()
    else:
        print("Please choose a valid option.")
    

# Main loop of the program
while True:

    # Show menu
    menu()

    try:
        # Get user choice
        choice = int(input("Choose an option: "))

        # Execute selected option
        handle_option()
    
    except ValueError:
        print("Choice a valid option:")

