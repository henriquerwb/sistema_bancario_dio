menu = """
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

 => """
 
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    print("Depósito")
    valor_deposito = float(input("Digite o valor a ser depositado: "))
    while valor_deposito <= 0:
        print("Valor inválido. Digite novamente")
        valor_deposito = float(input("Digite o valor a ser depositado: "))
    saldo += valor_deposito
    extrato.append(f'DEPÓSITO: {valor_deposito} R$')

def sacar():
    global saldo, numero_saques, extrato
    print("Saque")
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque > saldo:
        print("Saldo indisponível. Tente novamente.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Você já atingiu o limite de saques diários.")
    elif valor_saque > limite:
        print("O valor máximo para cada saque é de 500 R$")
    else:
        print("Saque realizado com sucesso.")
        saldo -= valor_saque
        numero_saques += 1
        extrato.append(f'SAQUE: {valor_saque} R$')

def exibir_extrato():
    print("Extrato")
    print(extrato)
    print(f'Saldo atual: {saldo} R$')

while True:
    opcao = input(menu)

    if opcao == "d":
        depositar()

    elif opcao == "s":
        sacar()

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Tente novamente.")
