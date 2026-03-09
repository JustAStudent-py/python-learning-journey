# Product Management System
# This program allows the user to add products, list them, and update stock.

menu_choice = ""
products = []  # List that stores all product dictionaries


while True:

    # Display main menu
    print("\n" + "=" * 40)
    print("        PRODUCT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("[1] Add product")
    print("[2] List products")
    print("[3] Update stock")
    print("[4] Exit")
    print("=" * 40)

    # Ask the user to choose an option
    menu_choice = input("Choose an option: ").strip()

    # Exit the system
    if menu_choice == "4":
        print("\nExiting the system... Goodbye!")
        break

    # ------------------------------------------------
    # OPTION 1 — ADD PRODUCT
    # ------------------------------------------------
    elif menu_choice == "1":

        print("\n--- Add New Product ---")

        # Collect product information
        name = input("Enter product name: ").strip().lower()
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        # Create product dictionary
        product = {
            "name": name,
            "price": price,
            "stock": stock
        }

        # Add product to the list
        products.append(product)

        print("\n Product successfully registered!")

    # ------------------------------------------------
    # OPTION 2 — LIST PRODUCTS
    # ------------------------------------------------
    elif menu_choice == "2":

        print("\n--- Registered Products ---")

        # Check if there are products in the system
        if len(products) == 0:
            print("⚠ No products registered yet.")

        else:
            # Loop through products and display them
            for index, product in enumerate(products, start=1):

                print("-" * 30)
                print(f"Product #{index}")
                print(f"Name : {product['name']}")
                print(f"Price: ${product['price']}")
                print(f"Stock: {product['stock']}")

            print("-" * 30)

    # ------------------------------------------------
    # OPTION 3 — UPDATE PRODUCT STOCK
    # ------------------------------------------------
    elif menu_choice == "3":

        print("\n--- Update Product Stock ---")

        product_name = input("Enter product name: ").strip().lower()

        found = False  # Flag to check if product exists

        # Search for the product in the list
        for product in products:

            if product["name"] == product_name:

                new_stock = int(input("Enter new stock value: "))
                product["stock"] = new_stock

                print("\n Stock updated successfully!")
                found = True
                break

        # If product was not found
        if not found:
            print("\n Product not found.")

    # ------------------------------------------------
    # INVALID MENU OPTION
    # ------------------------------------------------
    else:
        print("\n Invalid option. Please select a valid menu number.")