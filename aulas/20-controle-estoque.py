import os
os.system("cls")

print("BEM VINDO AO SISTEMA DE CONTROLE DE ESTOQUE")

produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))

if quantidade <= 5:
    print("estoque baixo, é necessário fazer um pedido.")

else:
    print("estoque suficiente, não é necessário fazer um pedido.")
