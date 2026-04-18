import os
os.system("cls")

# primeira etapa - entrada 

print("bem vindo ao conversor de temperatura")

temperatura01 = float(input("coloque um numero de temperatura que deseja converter:"))

# segunda etapa - processamento

def fahrenheit_para_celsius(f:float):
    return(9 * temperatura01 + 160) / 5

# terceira etapa - saida

print("a conversao de celsius para fahrenheit é:",fahrenheit_para_celsius(temperatura01))

