import os
os.system("cls")

print("BEM VINDO A CALCULADORA VIRTUAL")

numero01 = float(input("digite o primeiro numero:"))
numero02 = float(input("digite o segundo numero:"))

print("escolha uma operação")
print("+ - Adição")
print("- - Subtração")
print("* - Multiplicação")
print("/ - divisão")

opreracao = input("informe sua operação que escolheu:")

if(opreracao == "+"):
    resultado = numero01 + numero02

elif(opreracao == "-"):
    resultado = numero01 - numero02

elif(opreracao == "*"):
    resultado = numero01 * numero02

elif(opreracao == "/"):
    resultado = numero01 / numero02

else:
    print("operação invalida!")

print("=" * 30)
print(f"operação escolhida: {opreracao}")
print(f"resultado: {resultado}")




  
