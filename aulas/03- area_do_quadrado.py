import os
os.system("cls")

print("descubra se o quadrado e grande,medio ou pequeno")
# fazendo  o quadrado
x=float(input('escreva o valor do X: '))
y=float(input('escreva o valor do y: '))
# área do calculo
a=x*y
# mostrando se é grande, medio ou pequeno
if a >= 100:
    print('grande')

elif a <= 50:
    print(' medio')

else:
    print('pequeno')

input("aperte espaço para sair")