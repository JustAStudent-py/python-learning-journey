# Restaurant Order System

# Display menu
print("====== MENU ======")
print("[1] Sandwich:      $2.0")
print("[2] Orange Juice:  $3.0")
print("[3] Cheesecake:    $2.5")
print("[4] Applepie:      $4.0")
print("[5] Exit")
print("==================")

# Variable to store the total price
total = 0

# Variable to store the user option
option = ""

# List to store the cart items
cart = []

# Loop runs until the user chooses option "5" (Exit)
while option != "5":
    
    # Ask the user to choose an item
    option = input("Choose your items: ")
    
    
    # Option 1 - Add Sandwich
    if option == "1":
        
        cart.append("Sandwich")   # Add item to cart
        total += 2.0              # Add price to total
        
        print(f"Total: ${total:.2f}")
        print(f"Cart: {cart}")


    # Option 2 - Add Orange Juice
    elif option == "2":
        
        total += 3.0
        cart.append("Orange Juice")
        
        print(f"Total: ${total:.2f}")
        print(f"Cart: {cart}")


    # Option 3 - Add Cheesecake
    elif option == "3":
        
        total += 2.5
        cart.append("Cheesecake")
        
        print(f"Total: ${total:.2f}")
        print(f"Cart: {cart}")


    # Option 4 - Add Applepie
    elif option == "4":
        
        total += 4.0
        cart.append("Applepie")
        
        print(f"Total: ${total:.2f}")
        print(f"Cart: {cart}")
        

    # Option 5 - Exit and show final cart
    elif option == "5":
        
        print("==== FINAL CART ====")
        print(f"Cart: {cart}")
        print(f"Total price: ${total:.2f}")


    # If the user types an invalid option
    else:
        print("Invalid option. Please try again.")