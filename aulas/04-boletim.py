import os
os.system("cls")

# primeira etapa - entrada

print("bem vindo ao boletim virtual")

nota01 = float(input("entre com a primeira nota:"))
nota02 = float(input("entre com a segunda nota:"))
nota03 = float(input("entre com a terceira nota:"))

# segunda etapa - processamento 

media = (nota01 + nota02 + nota03) / 3 

if(media >= 6):
    print("voce foi aprovado!")

else:

    print("voce foi reprovado!")

    

# terçeira etapa - saida

print(f"sua media foi:{media}")




