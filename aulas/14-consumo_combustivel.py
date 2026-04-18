import os
os.system("cls")

print("BEM VINDO AO SIMULADOR DE CONSUMO DE COMBUSTIVEL")

quantidade_km = (int(input("digite a quantidade de quilometros percorridos: ")))
combustivel_gasto =(int(input("digite a quantidade de combustivel gasto: ")))

consumo = quantidade_km / combustivel_gasto

print(f"o consumo medio de combustivel do veiculo foi: {consumo} litros")
