import os
os.system("cls")

print("BEM VINDO AO PEDAGIO")
print("escolha o tipo de veiculo:")
print("CARRO")
print("MOTO")
print("CAMINHÃO")

selecao_veiculo = input("informe o tipo de veiculo que escolheu: ")

if selecao_veiculo == "carro":
    tarifa = 10
    print("a tarifa é de 10 r$")

elif selecao_veiculo == "moto":
    tarifa = 5
    print("a tarifa é de 5 r$")

elif selecao_veiculo == "caminhão":
    tarifa = 20
    print("a tarifa do caminhão é de 20 r$")

else:
    print("tipo invalido")


input("pressione o enter para sair...")
