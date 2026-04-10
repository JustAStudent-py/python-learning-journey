# ==============================
# DATA INITIALIZATION
# ==============================

# Raw data
names = ["Notebook", "Mouse", "Keyboard"]
prices = [2500, 100, 300]

# Structured data
products = []

# Combine names and prices into a list of dictionaries
for i in range(len(names)):
    product = {
        'name': names[i],
        'price': prices[i]
    }

    products.append(product)


# ==============================
# BUSINESS LOGIC
# ==============================

def filter_product(products):
    """
    Filters products with price greater than or equal to 200.
    """
    filtered = []

    for product in products:
        if product['price'] >= 200:
            filtered.append(product)

    return filtered


def find_product_by_name(products, name):
    """
    Searches for a product by name (case insensitive).
    Returns the product if found, otherwise None.
    """
    for product in products:
        if product['name'].lower() == name.lower():
            return product
    
    return None


# ==============================
# OUTPUT: FILTERED PRODUCTS
# ==============================

print("\n=== FILTERED PRODUCTS (price >= 200) ===")

result = filter_product(products)

if result:
    for product in result:
        print(f"- {product['name']} | Price: {product['price']}")
else:
    print("No products match the filter.")


# ==============================
# INPUT: SEARCH PRODUCT
# ==============================

print("\n=== SEARCH PRODUCT ===")

name = input("Enter a product name: ").strip()

result = find_product_by_name(products, name)

if result:
    print("\nProduct found:")
    print(f"Name: {result['name']}")
    print(f"Price: {result['price']}")
else:
    print("Product not found.")

