# Saldo inicial da conta
saldo = 0


def mostrar_saldo():
    """
    Exibe o saldo atual do usuário.
    """
    if saldo == 0:
        print("Sem saldo.")
    else:
        print(f"Saldo: ${saldo:.2f}")


def depositar_valor():
    """
    Permite ao usuário depositar um valor na conta.
    """
    global saldo

    try:
        # Solicita o valor do depósito
        valor_deposito = float(input("Digite o valor que deseja depositar: $"))
    except ValueError:
        print("Por favor digite um número válido.")
        return 0

    # Verifica se o valor é positivo
    if valor_deposito > 0:
        saldo += valor_deposito
        print(f"Depósito: ${valor_deposito:.2f} | Novo saldo: ${saldo:.2f}")
        return saldo
    else:
        print("O valor do depósito precisa ser maior que zero.")


def sacar_saldo():
    """
    Permite ao usuário sacar um valor da conta.
    """
    global saldo

    # Verifica se há saldo disponível
    if saldo <= 0:
        print("Sem saldo disponível.")
        return

    try:
        # Solicita o valor do saque
        valor_saque = float(input("Digite o valor que deseja sacar: $"))
    except ValueError:
        print("Digite um valor válido.")
        return 0

    # Verifica se o saque é maior que o saldo
    if valor_saque > saldo:
        print("Valor do saque maior que o saldo disponível.")
    else:
        saldo -= valor_saque
        print(f"Saque: ${valor_saque:.2f} | Novo saldo: ${saldo:.2f}")
        return saldo


def menu():
    """
    Exibe o menu principal e retorna a opção escolhida pelo usuário.
    """
    print("=" * 40)
    print("Caixa Eletrônico")
    print("=" * 40)
    print("1 - Ver Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    print("=" * 40)

    try:
        return int(input("Escolha uma opção (1-4): "))
    except ValueError:
        print("Entrada inválida. Escolha um número entre 1 e 4.")
        return 0


# Mapeamento das opções para funções
options = {
    1: mostrar_saldo,
    2: depositar_valor,
    3: sacar_saldo,
}


# Loop principal do sistema
while True:
    option = menu()

    if option == 4:
        print("Obrigado por usar o sistema.")
        break
    elif option in options:
        options[option]()  # Executa a função correspondente
    else:
        print("Opção inválida. Escolha um número entre 1 e 4.")