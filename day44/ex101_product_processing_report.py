products = [
    {"name": "Notebook", "price": 3000},
    {"name": "Mouse", "price": 100},
    {"name": "Teclado", "price": 200},
    {"name": "Monitor", "price": 900}
]

raw_products = [
    "Notebook - R$3000",
    "Mouse - R$100",
    "Teclado - R$200",
    "Monitor - R$900"
]


# Converte lista de strings em lista de dicionários
def parse_products(raw_products):
    result = []

    for item in raw_products:
        parts = item.split("-")

        # Ignora itens inválidos
        if len(parts) < 2:
            continue
    
        name = parts[0].strip()
        price = parts[1].strip()

        product = {
            'name': name,
            'price': int(price.replace("R$", ""))
        }

        result.append(product)
    
    return result


# Filtra produtos com preço acima de 500
def filter_expensive(products):
    result = []

    for product in products:
        if product['price'] > 500:
            result.append(product)
        
    return result


# Retorna apenas os nomes dos produtos
def get_product_names(products):
    result = []

    for product in products:
        result.append(product['name'])

    return result


# Conta quantos produtos são caros (>500)
def count_expensive(products):
    count = 0
    
    for product in products:
        if product['price'] > 500:
            count += 1
            
    return count


# Gera resumo geral dos produtos
def generate_report(products):
    expensive_products = filter_expensive(products)
    
    return {
        'total': len(products),
        'expensive': count_expensive(products),
        'expensive_products': get_product_names(expensive_products)
    }


# ==============================
# OUTPUT
# ==============================

filtered = filter_expensive(products)

print("\nExpensive products:")
for p in filtered:
    print(f"- {p['name']} | {p['price']}")


products_names = get_product_names(products)

print("\nProduct names:")
for name in products_names:
    print(f"- {name}")


quantify_expensive_items = count_expensive(products)

print(f"\nTotal expensive products: {quantify_expensive_items}")


parsed_products = parse_products(raw_products)

print("\nOrganized raw products:")
for p in parsed_products:
    print(f"- {p['name']} | {p['price']}")


report_items = generate_report(products)

print("\nReport:")
print(f"Total: {report_items['total']}")
print(f"Expensive: {report_items['expensive']}")

print("Expensive product names:")
for name in report_items['expensive_products']:
    print(f"- {name}")