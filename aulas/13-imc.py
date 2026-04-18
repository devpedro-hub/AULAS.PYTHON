import os
os.system("cls")

print("BEM VINDO AO CALCULADOR DE IMC")

peso = int(input("digite seu peso: "))
altura = float(input("digite sua altura:"))

imc = peso / (altura * altura)

if imc < 16.9:
    print("muito abaixo do peso")

elif imc > 17 and imc < 18.4:
    print("abaixo do peso")

elif imc >= 18.5 and imc < 24.9:
    print("peso normal")

elif imc >= 25 and imc < 29.9:
    print("acima do peso")

elif imc >= 30 and imc < 34.9:
    print("obesidade grau 1")

elif imc >= 35 and imc < 40:
    print("obesidade grau 2")

else:
    print("obesidade grau 3")

input("pressione espaço para sair")
