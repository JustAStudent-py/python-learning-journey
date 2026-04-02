# Armazenamento em memória
users = []
emails = set()


def create_user(users, emails):
    """
    Cria um novo usuário após validações básicas.
    Não altera estrutura, apenas adiciona na lista/set.
    """

    print("\n=== CREATE USER ===")

    name = input("Enter user name: ").strip().title()
    email = input("Enter user email: ").strip().lower()

    # Validação de nome
    if not name:
        print(" Invalid name. Please try again.")
        return users

    # Validação simples de email
    if "@" not in email or "." not in email:
        print(" Invalid email format.")
        return users

    # Verifica duplicidade
    if email in emails:
        print(" User already exists.")
        return users

    # Estrutura do usuário
    user = {
        "name": name,
        "email": email
    }

    # Persistência em memória
    users.append(user)
    emails.add(email)

    print("User registered successfully!")


def show_users(users):
    """
    Exibe todos os usuários cadastrados.
    """

    print("\n=== USER LIST ===")

    if not users:
        print(" No users found.")
        return users

    # Lista usuários com índice
    for index, user in enumerate(users, start=1):
        print(f"[{index}] Name: {user['name']} | Email: {user['email']}")


def menu():
    """
    Exibe o menu principal e captura a opção do usuário.
    """

    print("\n" + "=" * 40)
    print("        USER MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1 - Create user")
    print("2 - Show users")
    print("3 - Exit")
    print("=" * 40)

    try:
        return int(input(" Choose an option (1-3): "))
    except ValueError:
        # Retorna 0 para cair no fluxo de opção inválida
        return 0


# Loop principal do sistema
while True:
    option = menu()

    if option == 3:
        print("\nClosing system... See you!")
        break

    elif option == 1:
        create_user(users, emails)

    elif option == 2:
        show_users(users)

    else:
        print(" Invalid option. Please choose between 1 and 3.")