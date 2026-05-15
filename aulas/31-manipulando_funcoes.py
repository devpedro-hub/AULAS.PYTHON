
import funcoes

funcoes.limpar_tela()

input("BEM VINDO AO SISTEMA DE CALCULADORA, pressione enter para continuar...")

resposta_usuario = "sim"

while(resposta_usuario == "sim"):
    
    funcoes.exibir_menu() # chamar a funcao para exibir o menu

    opcao = int(input("digite a opcao desejada: "))

    numero1 = int(input("digite o primeiro numero: "))
    numero2 = int(input("digite o segundo numero: "))
     
    funcoes.limpar_tela() # chamar a funcao para limpar a tela

    if opcao == 1:
        resultado = funcoes.somar(numero1, numero2) # chamar a funcao para somar os numeros
        print(f"o resultado da soma é: {resultado}")

    elif opcao == 2:
        print(f"o resultado da subtração é: {funcoes.subtrair(numero1, numero2)}") # chamar a funcao para subtrair os numeros

    elif opcao == 3:
        print(f"o resultado da multiplicação é:  {funcoes.multiplicar(numero1, numero2)}") # chamar a funcao para multiplicar os numeros

    elif opcao == 4:
        print(f"o resultado da divisão é: {funcoes.dividir(numero1, numero2)}") # chamar a funcao para dividir os numeros

    else:
        print("opção inválida, por favor escolha uma opção válida")

    resposta_usuario = input("deseja realizar outra operação (sim/não): ")