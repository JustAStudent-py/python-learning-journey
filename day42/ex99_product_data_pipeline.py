
# Exibe resumo final
raw_products = [
    "Notebook - R$3000",
    "Mouse - R$100",
    "Teclado - R$200",
    "Monitor - R$900",
    "Item inválido",
    "Cadeira - R$1500"
]


def create_dict(raw_products):
    # Converte lista de strings em lista de dicionários estruturados
    # Ignora entradas inválidas (sem separador "-")
    result = []
    
    for item in raw_products:
        parts = item.split("-")

        # Se não tiver nome + preço, ignora
        if len(parts) < 2:
            continue
        
        name = parts[0].strip()
        price = parts[1].strip()

        # Remove "R$" e converte para inteiro
        product = {
            "name": name,
            "price": int(price.replace("R$", ""))
        }

        result.append(product)

    return result


def only_greater_500(products):
    # Filtra produtos com preço acima de 500
    # Obs: mantém comportamento original recriando a lista internamente
    result = []

    products = create_dict(raw_products)

    for item in products:
        if item['price'] > 500:
            result.append(item)
    
    return result


def generate_report():
    # Gera um resumo dos dados processados
    # Inclui total de produtos, quantidade filtrada e nomes
    names = []
    
    products = create_dict(raw_products)
    filtered = only_greater_500(products)
    
    for item in filtered:
        names.append(item['name'])
        
    return {
        'total': len(products),
        'greater_than_500': len(filtered),
        'names': names
    }


# Execução principal (simula fluxo de uso real)

products = create_dict(raw_products)
filtered = only_greater_500(products)
report = generate_report()


# Exibe todos os produtos já tratados
print("\n=== ALL PRODUCTS ===")
for p in products:
    print(f"{p['name']} - {p['price']}")


# Exibe apenas produtos filtrados
print("\n=== FILTERED PRODUCTS (PRICE > 500) ===")
for p in filtered:
    print(f"{p['name']} - {p['price']}")


# Exibe resumo final
print("\n=== REPORT ===")
print(f"Total: {report['total']}")
print(f">500: {report['greater_than_500']}")

for name in report['names']:
    print(f"- {name}")
print(f"Total: {report['total']}")
print(f"Preço maior que $500: {report['greater_than_500']}")

