products = []

def add_product(products):
    
    name = input("Whats is the product: ").lower()
    price = float(input("Insert the price of the product: $"))
    discount = input("The product have discount? (s/n) ").lower()

    
    product = {
        "name": name,
        "price": price,
        "discount": discount
    }

    products.append(product)

def apply_discount(products):
    
    product_discount = []

    for product in products:
        if product["discount"] == "s":
            product_discount.append(product)
            product_discount['price'] *= 0.90

    
    return product_discount

def show_products(products):
    
    print("\n Products :")

    if not products:
        print("No products found: ")
    else:
        for product in products:
            print(f"Products: {product['name']} | Price: ${product['price']}")

   

def handle_option(choice):
    options = actions.get(choice)
    
    if choice in options:
        [choice]()
    else:
        print("Please choose a valid option.")
    
    return options

def menu():
    
    print("=" * 40)
    print("CLI Eletronic box")
    print("=" * 40)
    print("1- Sum products.")
    print("2 - Calculate discount.")
    print("3 - Show Products.")
    print("4-  Exit.")

    try:
        return int(input("Choose a option: "))
    except ValueError:
        return 0

actions = {
    1: add_product,
    2: apply_discount,
    3: show_products
}



while True:

    menu()

    choice = int(input("Choose an option: "))

    handle_option(choice)
    



    
    


    
    
