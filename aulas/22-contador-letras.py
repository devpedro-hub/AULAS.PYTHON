import os
os.system("cls")

print("BEM VINDO AO CONTADOR DE LETRAS")

palavras = input("Digite uma palavra: ")
contador_letras = len(palavras)
print(f"A palavra {palavras} tem {contador_letras} letras.")
input("Pressione Enter para sair...")