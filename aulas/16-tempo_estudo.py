import os
os.system("cls")

print("BEM VINDO AO CALCULADO DE TEMPO DE ESTUDO")

horas_estudo = (int(input("digite quantas horas vc estuda: ")))

if horas_estudo < 2:
    print("pouco estudo")

elif horas_estudo == 4:
    print("estudo medio")

elif horas_estudo > 4:
    print("muito estudo")
