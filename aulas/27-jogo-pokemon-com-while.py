import os
import random
import time
import pygame

os.system("cls")

#Musica
pygame.mixer.init()
pygame.mixer.music.load("musica_abertura_pokemon.mp3")
pygame.mixer.music.play()

vida_jogador = 50
vida_inimigo = 50

print("Bem vindo a batalha pokémon em python!")
nome = input("Informe seu nome?:")

while(vida_jogador > 0 and vida_inimigo > 0):
    os.system("cls")
    print(f"Vida: {vida_jogador} | Vida inimigo: {vida_inimigo}")

    print("Faça sua Jogada")
    print("[1] - Atacar")
    print("[2] - Curar")
    print("[3] - Fugir")

    op_jogador = int(input("Escolha uma opção:"))
    op_inimigo = random.randint(1,3)

    #Meu Turno
    #Atacou
    if(op_jogador == 1):
        vida_inimigo -= 10

    #Curou
    elif(op_jogador == 2):
        vida_jogador += 5

    #Fugiu
    elif(op_jogador == 3):
        print("Você fugiu!")
        vida_jogador = 0

    print("Iniciando a jogada do inimigo em 3 segundos...")
    time.sleep(3)
  
    #Turno do Inimigo
    if(op_inimigo == 1):
        print(f"O inimigo escolheu: Atacar!")
        time.sleep(3)
        vida_jogador -= 10
    elif(op_inimigo == 2):
        print(f"O inimigo escolher: Curar!")
        time.sleep(3)
        vida_inimigo += 5
    elif(op_inimigo == 3):
        print("O inimigo escolheu: Fugir!")
        vida_inimigo = 0
        time.sleep(3)

#Verificando quem foi o ganhador
if(vida_jogador > vida_inimigo):
    print("Parabéns você venceu!")

else:
    print("Game Over - Você perdeu!")


