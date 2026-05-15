import os 

# sistema principal 

os.system("cls")


def exibir_catalogo(filmes):
    os.system("cls")
    print("   catalogo de filmes   ")

    for item in filmes:
        print(f"titulo: {item['titulo']}")
        print(f"genero: {item['genero']}")




def carregar_menu_adimin():
    os.system("cls")
    print(" autenticação ")
    usuario = input("digite seu nome de usuario:  ")
    senha = input("informe sua senha:  ")

    if(usuario != "adimin" and senha != 123):
        input("acesso negado")
        return
    
    while True:
        os.system("cls")
        print("MENU DO ADIMINISTRADOR")
        print("[1] - cadastrar filme")
        print("[2] - ver catalogo")
        print("[3] - top e flop")
        print("[4] - voltar")

        op = int(input("selecione uma opção:  "))

        if(op == 1):
            os.system("cls")
            print("cadastro dos filmes")
            titulo = input("titulo do filme:  ")
            genero = input("genero do filme:  ")

            filme = {

                "titulo": titulo,
                "genero": genero,
                "avaliacoes": [],
                "media": 0,
                "classificacao": "sem avaliações",
                "disponivel": True,
                "cliente": None,

            }

            filmes.append(filme)
            print("filme colocado com sucesso")
            input("pressione ENTER  para continuar....")

        elif(op == 2):
            exibir_catalogo(filmes)
            input("pressione ENTER para continuar")
        
       


        elif(op == 4):
            break



# listas de filmes - banco de dados

filmes = []

while True:
    os.system("cls")

    print("BEM VINDO A LOCADORA CINEFLIX ")
    print("[1] - entrar como cliente")
    print("[2] - entrar como administrador")
    print("[3] - sair")

    op = int(input("escolha uma opção:   "))

    if(op == 1):
        print("entrou como cliente")
    
    elif(op == 2):
        carregar_menu_adimin()
        

    elif(op == 3):
        print("obrigado por usar o sistema")
        input("pressione <enter> para sair...")
        break