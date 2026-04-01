# Saldo inicial da conta
saldo = 0

# lista para armazenar o historico
historico = []

def mostrar_saldo(saldo, historico): #Exibe o saldo atual do usuário.
    
    if saldo == 0:
        print("Saldo atual: $0.00.")
    else:
        print(f"Saldo: ${saldo:.2f}")
    
    return saldo, historico

def depositar_valor(saldo, historico):  #Permite ao usuário depositar um valor na conta.
    
    try:
        # Solicita o valor do depósito
        valor_deposito = float(input("Digite o valor que deseja depositar: $"))
    except ValueError:
        print("Por favor digite um número válido.")
        return saldo, historico

    # Verifica se o valor é positivo
    if valor_deposito > 0:
        saldo += valor_deposito
        historico.append(f"Deposito: ${valor_deposito:.2f}")
        print(f"Depósito: ${valor_deposito:.2f} | Novo saldo: ${saldo:.2f}")
    else:
        print("O valor do depósito precisa ser maior que zero.")
    
    return saldo, historico
    
def sacar_saldo(saldo, historico):  #Permite ao usuário sacar um valor da conta.
    
   # Verifica se há saldo disponível
    if saldo <= 0:
        print("Sem saldo disponível.")
        return saldo, historico

    try:
        # Solicita o valor do saque
        valor_saque = float(input("Digite o valor que deseja sacar: $"))
    except ValueError:
        print("Digite um valor válido.")
        return saldo, historico

    # Verifica se o saque é maior que o saldo
    if valor_saque > saldo:
        print("Valor do saque maior que o saldo disponível.")
    else:
        saldo -= valor_saque
        historico.append(f"Saque: ${valor_saque:.2f}")
        print(f"Saque: ${valor_saque:.2f} | Novo saldo: ${saldo:.2f}")
    
    return saldo, historico    

def mostrar_historico(saldo, historico): # Função para mostrar o histórico
    
    # verifica se a lista de historicos está vazia.
    if not historico:
        print("Sem transações realizadas até agora.")
    
    else:
        print("\n=== HISTORICO ===")
        for item in historico:
            print(item)
    
    return saldo, historico

def menu(): # Exibe o menu principal e retorna a opção escolhida pelo usuário.
    
    print("=" * 40)
    print("Caixa Eletrônico")
    print("=" * 40)
    print("1 - Ver Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Mostrar Historico")
    print("5- Sair")
    print("=" * 40)

    # validar entrada do usuário
    try:
        return int(input("Escolha uma opção (1-5): "))
    except ValueError:
        print("Entrada inválida. Escolha um número entre 1 e 5.")
        return 0

# Mapeamento das opções para funções
options = {
    1: mostrar_saldo,
    2: depositar_valor,
    3: sacar_saldo,
    4: mostrar_historico
}

# Loop principal do sistema
while True:
    option = menu()

    if option == 5:
        print("Obrigado por usar o sistema.")
        break
    elif option in options:
        saldo, historico = options[option](saldo, historico)  # Executa a função correspondente
    else:
        print("Opção inválida. Escolha um número entre 1 e 5.")