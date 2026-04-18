import os
os.system("cls")

print("BEM VINDO AO PROGRAMAS DE PAGAMENTOS DA ESCOLA")

nivel_professor = input("digite o nível do professor: ")
quantidade_aulas = int(input("digite a quantidade de aulas: ")) 

if nivel_professor == "nivel1":
    valor_aula = 12

elif nivel_professor == "nivel2":
    valor_aula = 17
elif nivel_professor == "nivel3":
    valor_aula = 25
else:
    print("nível do professor inválido")
    exit()

total_pagamento = quantidade_aulas * valor_aula
print(f"o total do pagamento para o professor é: r$ {total_pagamento}")