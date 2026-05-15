import os
import funcoes
os.system("cls")

def exibir_menu():

    print("1 - REAL para dolar")
    print("2 - DOLAR para real")
    print("3 - sair")

def converter_real_para_dolar(quantia_real, taxa_dolar):
    total_dolar = quantia_real / taxa_dolar
    return total_dolar

def converter_dolar_para_reais(quantia_dolar, taxa_reais):
    total_reais = quantia_dolar * taxa_reais
    return total_reais

def sair():
    input("obrigado por usar o sistema, aperte enter para sair...")
    exit()


while True:
    
    funcoes.limpar_tela()

    print("BEM VINDO AO CONVERSOR DE MOEDAS")

    exibir_menu()

    opcao = int(input("qual opção deseja escolher:  "))

    # converter

    if(opcao == 1):
        quantia_real = float(input("informe a quantia em real:   "))
        taxa_dolar = float(input("informe a cotação do dolar:    "))

        total_dolar = converter_real_para_dolar(quantia_real,taxa_dolar)

        print(f"o total sera de: {total_dolar}")
        input("pressione ENTER para continuar")


    elif(opcao == 2):
        quantia_dolar = float(input("informe a quantia em dolar:    "))
        taxa_reais = float(input("informe a cotação do real:   "))

        total_reais = converter_dolar_para_reais(quantia_dolar, taxa_reais)

        print(f"o total sera de: {total_reais}")
        input("pressione ENTER para continuar")


    elif(opcao == 3):
        sair()









