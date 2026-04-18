import os
os.system("cls")

print("BEM VINDO AO CALCULADOR DE IDADE")
nascimento_pessoa = float(input("insira seu mes de nascimento:"))
ano_atual = float(input("insira o ano atual:"))

calculo = (nascimento_pessoa + ano_atual) 

print(f"sua idade será de:{calculo}")