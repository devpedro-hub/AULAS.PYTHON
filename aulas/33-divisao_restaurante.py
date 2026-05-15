import os 
import funcoes

funcoes.limpar_tela()
while True:
    funcoes.exibir_menu()

    opcao = int(input("qual opção deseja escolher:  "))

    if opcao == 4:
        funcoes.sair()
        break

    compra_total = float(input("informe o valor total da compra:   "))
    quantidade_pessoas = int(input("informe a quantidade de pessoas:   "))
    
    taxa_cartao = 3/100 
    taxa_garcom = 10/100 #10% de taxa de garcom
    taxa_vr_va = 2/100

    if(opcao == 1):
        valor_por_pessoa = funcoes.dividir(compra_total, quantidade_pessoas, taxa_garcom)
        print(f"o valor por pessoa incluindo taxa de garcom sera de: {valor_por_pessoa}")
        
    
    elif(opcao == 2):
        valor_por_pessoa = funcoes.dividir_cartao(compra_total, quantidade_pessoas, taxa_cartao, taxa_garcom)
        print(f"o valor por pessoa incluindo taxa de cartão e garcom sera de: {valor_por_pessoa}")
        
    
    elif(opcao == 3):
        valor_por_pessoa = funcoes.dividir_vr_va(compra_total, quantidade_pessoas, taxa_vr_va, taxa_garcom)
        print(f"o valor por pessoa incluindo taxa de VR/VA e garcom sera de: {valor_por_pessoa}")
        
    continuar = input ("deseja continuar usando o sistema? (sim/não)")
    if continuar.lower() != "nao":
        funcoes.sair()
        break
    