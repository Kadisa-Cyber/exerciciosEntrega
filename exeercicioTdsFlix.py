""" 
Feito na aula de Projeto Back-End
Kauan Dias Santos
"""

import os
os.system('cls')

listaGenero = ['Ação', 'Comédia', 'Terror', 'Ficção', 'Romance', 'Aventura']

listaFilmes = [
    {
        'nome': 'Matrix',
        'genero': 'Ficção',
        'disponibilidade': 'Disponivel'
    },
    {
        'nome': 'O Poderoso Chefão',
        'genero': 'Ação',
        'disponibilidade': 'Indisponivel'
    },
    {
        'nome': 'Jumanji',
        'genero': 'Aventura',
        'disponibilidade': 'Disponivel'
    },
    {
        'nome': 'Como Se Fosse a Primeira Vez',
        'genero': 'Romance',
        'disponibilidade': 'Disponivel'
    },
    {
        'nome': 'Corra!',
        'genero': 'Terror',
        'disponibilidade': 'Indisponivel'
    }
]

listaDisponibilidade = ["Disponivel","Indisponivel"]

def cadastroFilme():
    os.system('cls')
    print("┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
    print("┃         Sistema de cadastro de filmes          ┃")
    print("┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")

    nomeFilme = input("Digite o nome do filme: ")

    for i,generos in enumerate(listaGenero):
        print(f"{i+1} - {generos}")
    
    opcaoFilme = len(listaGenero)+1
    while (opcaoFilme > len(listaGenero)) or (opcaoFilme < 1):
        opcaoFilme = int(input("Digite o numero do genero que deseja: "))
        if(opcaoFilme > len(listaGenero)) or (opcaoFilme < 1):
            print("Digite uma opcao valida!")
    generoFilme = listaGenero[opcaoFilme-1]

   
    for i,disp in enumerate(listaDisponibilidade):
         print(f"{i+1} - {disp}")
    opcaoDisponibilidade = len(listaDisponibilidade)+1
    while (opcaoDisponibilidade > len(listaDisponibilidade)) or (opcaoDisponibilidade < 1):
        opcaoDisponibilidade = int(input("Digite o numero da sua opção: "))
        if(opcaoDisponibilidade > len(listaDisponibilidade)) or (opcaoDisponibilidade < 1):
            print("Digite uma opcao valida!")
    
    disponibilidadeFilme = listaDisponibilidade[opcaoDisponibilidade-1]

    filme = {'nome': nomeFilme, 'genero':generoFilme, 'disponibilidade': disponibilidadeFilme}
    listaFilmes.append(filme)

    print(f"O filme {nomeFilme} foi cadastro com sucesso")

    sairInput = input("\n Digite enter para sair")

def exibirFilmes():

    os.system('cls')
    print("┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
    print("┃        Catalogo de filmess disponiveis         ┃")
    print("┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
    for i,filme in enumerate(listaFilmes):
        print(f"{filme['nome']} ━ {filme['genero']} ━ {filme['disponibilidade']}")
    
    sairInput = input("\n Digite enter para sair")

def consultaGenero():
    os.system('cls')

    print("┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
    print("┃              Consulta por genero               ┃")
    print("┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
    opcaoFilme = len(listaGenero)+1
    for i,generos in enumerate(listaGenero):
        print(f"{i+1} - {generos}")
    while (opcaoFilme > len(listaGenero)) or (opcaoFilme < 1):
        opcaoFilme = int(input("Digite o numero do genero que deseja: "))
        if(opcaoFilme > len(listaGenero)) or (opcaoFilme < 1):
            print("Digite uma opcao valida!")
    generoFilme = listaGenero[opcaoFilme-1]
    
    for filme in listaFilmes:
        if filme['genero'] == generoFilme:
            print(f"{filme['nome']} ━ {filme['genero']} ━ {filme['disponibilidade']}")
    
    sairInput = input("\n Digite enter para sair")

def alterarDisponibilidade():
    os.system('cls')
    print("┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
    print("┃       Alterar disponibilidade de itens         ┃")
    print("┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
    opcaoFilme = len(listaFilmes)+1
    print("Catalogo de filmes disponiveis \n ")
    for i,filme in enumerate(listaFilmes):
        print(f"{i+1} - {filme['nome']} ━ {filme['genero']} ━ {filme['disponibilidade']}")
    while (opcaoFilme > len(listaFilmes)) or (opcaoFilme < 1):
        opcaoFilme = int(input("Digite o numero da sua opção: "))
        if (opcaoFilme > len(listaFilmes)) or (opcaoFilme < 1):
            print("Digite uma opcao valida")
    filme = listaFilmes[opcaoFilme-1]

    if(filme['disponibilidade'] == "Disponivel"):
        print(f"A disponiibilidade do filme {filme['nome']} estava {filme['disponibilidade']} e agora está Indisponivel!")
        filme['disponibilidade'] = "Indisponivel"
    else:
        print(f"A disponiibilidade do filme {filme['nome']} estava {filme['disponibilidade']} e agora está Disponivel!")
        filme['disponibilidade'] = "Disponivel"

    sairInput = input("\n Digite enter para sair")

def filtrarGeneroDisponibilidade():
    os.system('cls')
    opcaoFilme = len(listaGenero)+1
    print("┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
    print("┃     Filtro por genero e disponibilidade        ┃")
    print("┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
    for i,generos in enumerate(listaGenero):
        print(f"{i+1} - {generos}")

    while (opcaoFilme > len(listaGenero)) or (opcaoFilme < 1):
        opcaoFilme = int(input("Digite o numero do genero que deseja: "))
        if(opcaoFilme > len(listaGenero)) or (opcaoFilme < 1):
            print("Digite uma opcao valida!")

    generoFilme = listaGenero[opcaoFilme-1]
    
    for filme in listaFilmes:
        if (filme['genero'] == generoFilme) and (filme['disponibilidade'] == "Disponivel"):
            print(f"{filme['nome']} - {filme['genero']} - {filme['disponibilidade']}")
    
    sairInput = input("\n Digite enter para sair")

invalido = False

while True:

    os.system('cls')

    if(invalido==True):
        print("Digite um numero válido! \n ")

    invalido = False

    print("                   Bem vindo 𝕋𝔻𝕊𝔽𝕃𝕀𝕏")
    print("┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
    print("┃ O que você deseja fazer?                           ┃")
    print("┃ 1 ━ Cadastrar filmes                               ┃")
    print("┃ 2 ━ Exibir filmes                                  ┃")
    print("┃ 3 ━ Consulta por genero                            ┃")
    print("┃ 4 ━ Alterar disponibilidade                        ┃")
    print("┃ 5 ━ Filtrar por genero e disponibilidade           ┃")
    print("┃ 6 ━ Sair                                           ┃")
    print("┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")

    opcao = int(input("O que você deseja fazer? (1-5): "))

    match opcao:
        case 1:
            cadastroFilme()
        case 2:
            exibirFilmes()
        case 3:
            consultaGenero()
        case 4:
            alterarDisponibilidade()
        case 5:
            filtrarGeneroDisponibilidade()
        case 6: 
            break
        case _:
            invalido = True