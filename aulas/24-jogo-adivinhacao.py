import os
import random
os.system("cls")

print("BEM VINDO AO JOGO DA ADIVINHAÇÃO")

usuario_palpite = (int(input("digite um palpite: ")))

numero_palpite = random.randint(1,10)

if usuario_palpite == numero_palpite:
    print("acertou")

else:
    print(f"errou, o numero era {numero_palpite}")





