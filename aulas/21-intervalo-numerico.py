import os
os.system("cls")

print("BEM VINDO AO CONTROLADOR DE INTERVALO NUMERICO")

numero_intervalo = int(input("Digite um número para verificar se ele está dentro do intervalo de 10 a 50: "))

if numero_intervalo >= 10 and numero_intervalo <= 50:
    print("O número está dentro do intervalo de 10 a 50.")
else:
    print("O número não está dentro do intervalo de 10 a 50.")

input("Pressione Enter para sair...")