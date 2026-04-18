import os
os.system("cls")

     # passo 1 - entrada e variaveis

print("calculadora de descontos")
nome_produto = input("entre com o nome do produto:")
preco = float(input("digite o preço do produto:"))
percentual_desconto = float(input("entre com o a % do desconto do produto"))

     # passo 2 - processamento

valor = preco * percentual_desconto / 100
preco_final = preco - percentual_desconto

     # passo 3 - saida

print("================================================")
print("preço original", preco, "- preço com desconto", preco_final)


