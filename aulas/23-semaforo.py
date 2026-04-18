import os
os.system("cls")

print("BEM VINDO AO SEMAFORO")

cor_semaforo = input("escreva uma das 3 cores do semaforo: ")

if cor_semaforo == "verde":
    print("pode passar")

elif cor_semaforo == "amarelo":
    print("atenção")

elif cor_semaforo == "vermelho":
    print("pare!")

else:
    print("cor invalida")


input("pressione enter para sair...")
