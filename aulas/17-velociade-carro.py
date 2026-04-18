import os
os.system("cls")

print("VEJA SE SUA VELOCIDADE ESTA NO LIMITE OU NÃO")

velocidade_carro = (int(input("digite a velocidade que seu carro percorreu: ")))

if velocidade_carro > 80:
    print("multado")

else:
    print("dentro do limite")