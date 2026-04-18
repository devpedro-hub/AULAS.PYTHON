import os
os.system("cls")

print("FAÇA SEU LOGIN ABAIXO")

nome_usuario = input("escreva seu nome de usuario: ")
senha_usuario = (int(input("digite sua senha: ")))


if nome_usuario == "admin" and senha_usuario == 123:
    print("acesso liberado")

else:
    print("acesso negado")


    



