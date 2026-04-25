products = [
    {"name": "Notebook", "price": 3000},
    {"name": "Mouse", "price": 100},
    {"name": "Teclado", "price": 200},
    {"name": "Monitor", "price": 900}
]


# Retorna nomes dos produtos com preço > 500
def get_expensive_names(products):
    result = []

    for product in products:
        if product['price'] > 500:
            result.append(product['name'])
    
    return result


# Gera um resumo simples dos produtos
def generate_report(products):
    expensive_products = get_expensive_names(products)

    return {
        'total': len(products),
        'expensive_names': expensive_products
    }


# Soma o preço total dos produtos
def get_total_price(products):
    total = 0

    for product in products:
        total += product['price']

    return total


# Calcula média de preço
def get_average_price(products):
    total_prices = get_total_price(products)
    
    if len(products) == 0:
        return None
    
    return total_prices / len(products)


# ==============================
# OUTPUT
# ==============================

average_prices = get_average_price(products)
print(f"\nAverage price: {average_prices:.2f}")


report = generate_report(products)

print("\nReport:")
print(f"Total products: {report['total']}")

filtered_products_names = get_expensive_names(products)

print("\nFiltered (>500):")
for name in filtered_products_names:
    print(f"- {name}")


total_price = get_total_price(products)
print(f"\nTotal price: {total_price:.2f}")