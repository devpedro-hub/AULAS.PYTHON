import os
import funcoes
os.system("cls")

print("BEM VINDO AO SISTEMA DE NOTAS")

funcoes.exibir_menu()

prosseguir_programa = input("deseja prosseguir com o programa (sim/não):     ")

while prosseguir_programa == "sim":
    os.system("cls")

    nota1 = print(int(input("digite a primeira nota: ")))
    nota2 = print(int(input("digite a segunda nota: ")))

    if nota1 and nota2 >= 6:
        print("voce foi aprovado")
    else:
        print("voce foi reprovado!")

    prosseguir_programa = input("deseja continuar o programa (sim/não)  ")  
print("muito obrigado por usar nosso sistema!")  

