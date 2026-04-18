import os
from time import time
os.system("cls")

print("BEM VINDO AO CAIXA ELETRONICO")

saldo = 1000

quer_prosseguir = input("voce deseja prosseguir (sim/nao)?  ")

while quer_prosseguir == "sim":
    os.system("cls")
    print("1 - Consultar saldo")
    print("2 - Sacar dinheiro")
    print("3 - Depositar dinheiro")
    print("4 - Sair")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        print(f"Seu saldo é: R${saldo}")
    elif opcao == 2:
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if valor_saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor_saque
            print(f"Saque realizado com sucesso! Seu novo saldo é: R${saldo}")
    elif opcao == 3:
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        saldo += valor_deposito
        time.sleep(3)
        print(f"Depósito realizado com sucesso! Seu novo saldo é: R${saldo}")
    elif opcao == 4:
        print("Obrigado por usar o caixa eletrônico. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    quer_prosseguir = input("Deseja realizar outra operação (sim/nao)?  ")
print("Obrigado por usar o caixa eletrônico. Até logo!")



