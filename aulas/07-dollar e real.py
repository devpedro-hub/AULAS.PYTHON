import os
os.system("cls")

# primeira etapa - entrada

print("BEM VINDO AO CONVERSOR DE DOLAR PARA REAL")
dollar = float(input("insira o valor do dollar:"))
cotacao_dollar = float(input("insira a cotação do dollar:"))

# segunda etapa - processamento

real = dollar * cotacao_dollar 

# terceira etapa - saida 

print(f"o valor do dollar convertido para reais é de: {real}")
input("pressione enter para sair")