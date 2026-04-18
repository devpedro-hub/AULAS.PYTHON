import os
os.system("cls")

print("BEM VINDO AO PROGRAMA DE RECEBIDOR DE PRODUTOS")

descricao = input("digite a descrição do produto: ")
quantidade_adiqui = int(input("digite a quantidade adquirida: "))
preco_unit = float(input("digite o preço unitário: "))

total = quantidade_adiqui * preco_unit
desconto = 0
if total <= 5:
    desconto = total * 0.02
    print("o desconto é de 2%")

elif total > 5 and total <= 10:
    desconto = total * 0.03
    print("o desconto é de 3%")

elif total > 10:
    desconto = total * 0.05
    print("o desconto é de 5%")

total_a_pagar = (total - desconto)

print(f"o valor total do produto {descricao} é: {total}")   
print(f"o desconto aplicado é de: {desconto}")
print(f"o total a pagar sera de: {total_a_pagar}")