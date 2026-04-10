# ==============================
# DATA INITIALIZATION
# ==============================

numbers = [1, 4, 6, 8, 9, 7, 10, 12, 15, 18, 20, 23, 26, 28, 32, 35, 39, 43, 52, 58, 62, 67, 70]

text = "  python, java, javascript, go, c++  "

users = [
    {"name": "Ana", "age": 17},
    {"name": "Carlos", "age": 22},
    {"name": "João", "age": 15},
    {"name": "Marina", "age": 30}
]

names = ["Notebook", "Mouse", "Teclado"]
prices = [3000, 100, 200]


# ==============================
# BUSINESS LOGIC
# ==============================

def organize_text(text):
    """
    Cleans and standardizes a comma-separated string.
    Output: list of uppercase trimmed items.
    """
    result = []
    
    text = text.strip()
    items = text.split(",")

    for item in items:
        result.append(item.strip().upper())

    return result


def analyze_greater_numbers(numbers):
    """
    Returns numbers greater than 20.
    """
    result = []

    for number in numbers:
        if number > 20:
            result.append(number)

    return result


def return_adults(users):
    """
    Filters users with age >= 18.
    """
    result = []
    
    for user in users:
        if user['age'] >= 18:
            result.append(user)

    return result


def show_adults_names(users):
    """
    Returns only the names of adult users.
    """
    result = []
    
    adults = return_adults(users)

    for adult in adults:
        result.append(adult['name'])
    
    return result


def create_products_list(names, prices):
    """
    Combines names and prices into a structured product list.
    """
    products = []

    for i in range(len(names)):
        product = {
            'name': names[i],
            'price': prices[i]
        }
        products.append(product)

    return products


# ==============================
# OUTPUT (CLI DISPLAY)
# ==============================

print("\n=== NUMBERS GREATER THAN 20 ===")

greater_numbers = analyze_greater_numbers(numbers)

if greater_numbers:
    for number in greater_numbers:
        print(f"- {number}")
else:
    print("No numbers found.")


print("\n=== ADULT USERS ===")

adults = return_adults(users)

if adults:
    for user in adults:
        print(f"- {user['name']} | Age: {user['age']}")
else:
    print("No adult users found.")


print("\n=== ADULT USER NAMES ===")

adult_names = show_adults_names(users)

if adult_names:
    for name in adult_names:
        print(f"- {name}")
else:
    print("No names found.")


print("\n=== ORGANIZED TEXT ===")

organized = organize_text(text)

for item in organized:
    print(f"- {item}")


print("\n=== PRODUCT LIST ===")

products = create_products_list(names, prices)

for product in products:
    print(f"- {product['name']} | Price: {product['price']}")