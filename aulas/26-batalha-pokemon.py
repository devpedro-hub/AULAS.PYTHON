import os
import random
import random
os.system("cls")

print("BEM VINDO A BATALHA DE POKEMON")

print("escolha seu pokemon")
print("1 - CHARMANDER")
print("2 - SQUIRTLER")
print("3 - BULBASAUR")

alternativa_pokemon = int(input("qual vc escolheu: "))

sortear_pokemon = random.randint(1,3)

print(f"computador escolheu: {sortear_pokemon}")

if alternativa_pokemon == sortear_pokemon:
    print("EMPATE")

elif alternativa_pokemon == 1 and sortear_pokemon == 3:
    print("FOGO VENCE")

elif alternativa_pokemon == 2 and sortear_pokemon == 1:
    print("ÁGUA VENCE")

elif alternativa_pokemon == 3 and   sortear_pokemon == 2:
    print("TERRA VENCE")

else:
    print("esse numero não condiz!")

input("aperte enter para sair...")



