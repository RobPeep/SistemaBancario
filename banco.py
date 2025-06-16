saldo = 0.0
extrato = ""
saques_realizados = 0
LIMITE_SAQUE = 500.0
LIMITE_SAQUES = 3

while True:
    print("\n=== MENU ===")
    print("D - Depositar")
    print("S - Sacar")
    print("E - Extrato")
    print("Q - Sair")
    print("============")

    opcao = input("Escolha uma opção: ").strip().upper()
    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Erro: o valor precisa ser positivo.")
    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Erro: o valor precisa ser positivo.")

        elif valor > saldo:
            print("Erro: saldo insuficiente.")

        elif valor > LIMITE_SAQUE:
            print(f"Erro: o valor excede o limite de R$ {LIMITE_SAQUE:.2f} por saque.")

        elif saques_realizados >= LIMITE_SAQUES:
            print("Erro: número máximo de saques diários atingido.")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques_realizados += 1
            print("Saque realizado com sucesso.")
    elif opcao == "E":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "Q":
        print("Obrigado por utilizar nosso sistema!")
        break
