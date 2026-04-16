import json

# Lista inicial de usuários
users = [
    {"name": "ana", "age": 17},
    {"name": "joao", "age": 22},
    {"name": "maria", "age": 19},
    {"name": "pedro", "age": 15}
]


# Exibe todos os usuários com índice
def show_users(users):
    for index, user in enumerate(users, start=1):
        print(f"User [{index}]: Name {user['name']} | Age {user['age']}")


# Filtra apenas usuários maiores de idade (>= 18)
def only_adults(users):
    adults = []

    for user in users:
        if user['age'] >= 18:
            adults.append(user)
        else:
            # Feedback para usuários que não atendem o critério
            print(f"{user['name']} is not an adult.")

    return adults


# Salva lista de usuários em arquivo JSON
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


# Carrega usuários do arquivo JSON
def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)
    return users


# Salva lista de adultos em arquivo separado
def save_adults(adults):
    with open("adults.json", "w") as file:
        json.dump(adults, file, indent=4)


# Carrega lista de adultos do arquivo
def load_adults():
    with open("adults.json", "r") as file:
        adults = json.load(file)
    return adults



# Salva usuários completos
save_users(users)

# Filtra e salva apenas adultos
adults = only_adults(users)
save_adults(adults)

# Carrega dados dos arquivos
loaded_users = load_users()
loaded_adults = load_adults()

# Exibe todos os usuários
show_users(loaded_users)

print("\nOnly adults:")

# Exibe apenas usuários adultos
show_users(loaded_adults)