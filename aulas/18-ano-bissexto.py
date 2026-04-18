import os
os.system("cls")

print("SOLUÇÃO PARA SABER O ANO BISSEXTO ESTÁ ABAIXO")

ano_selecionado = (int(input("digite o ano desejado: ")))

if ano_selecionado % 4 == 0 and ano_selecionado % 100 != 0 or ano_selecionado % 400 == 0:
    print("Ano bissexto")

else:
    print("Ano normal")