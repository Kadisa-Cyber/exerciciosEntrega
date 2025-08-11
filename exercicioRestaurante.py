
""" 
Feito na aula de Projeto Back-End
Kauan Dias Santos
"""

import os
os.system('cls')

opcoes = ["Yakisoba", "Sushi", "Temaki"]
precoTotal = 0
gorjetaGarcom = 0.10
comanda = [0,0,0,0]

cardapio = {
    'Yakisoba': 15.90,
    'Sushi': 25.00,
    'Temaki': 12.00
}

def mostrar_cardapio(cardapio):
    os.system('cls')
    print("\n========================================")
    print("Cardápio:")
    print("========================================")
    for prato, preco in cardapio.items():
        print(f"{prato} --------------- R${preco:.2f}")
    print("========================================\n ")

def fazer_pedido(cardapio, comanda):
    os.system('cls')
    precoTotal = 0
    escolher = True
    quantidadeComida = 0

    while escolher:
        print("\n========================================")
        print("Esse é o nosso cardápio: ")
        print("======================================== \n")
        for i, comida in enumerate(cardapio):
            print(f"{i + 1} - {comida} - R${cardapio[comida]:.2f}")
            # print(f"{i + 1} - {comida} - R${cardapio.get(comida):.2f}")
        print("========================================")

        opcaoComida = int(input("Qual você deseja escolher (1-3)?: "))
        comida = opcoes[opcaoComida - 1]
        quantidadeComida = int(input("Quantas unidades desse prato você deseja?: "))
        precoTotal += cardapio.get(comida) * quantidadeComida
        comanda[0] = precoTotal
        if opcaoComida == 1:
            comanda[1] += quantidadeComida
        elif opcaoComida == 2:
            comanda[2] += quantidadeComida
        elif opcaoComida == 3:
            comanda[3] += quantidadeComida

        opcaoContinuar = int(input("Você deseja continuar escolhendo? \n1- Sim\n2- Não\nOpcao: "))
        if opcaoContinuar == 2:
            return (comanda)

programaSair = True
precoTotal = 0

while programaSair:
    print("\n========================================")
    print("Bem-vindo(a) ao restaurante Kadisa \n        O que você deseja?")
    print("========================================\n")
    print("1- Mostrar cardápio \n2- Fazer pedido \n3- Sair")
    print("========================================\n")
    opcaoMenu = int(input("O que você deseja fazer (1-3)?: "))
    if opcaoMenu == 1:
        mostrar_cardapio(cardapio)  
    elif opcaoMenu == 2:
        listaFuncao =  fazer_pedido(cardapio, comanda)
        precoTotal += listaFuncao[0]
        os.system('cls') 
    elif opcaoMenu == 3:
        os.system('cls')
        print("\n========================================")
        print(f"Você pediu {comanda[1]} Yakisoba(s) ---- R${comanda[1] * cardapio.get('Yakisoba'):.2f}") 
        print(f"Você pediu {comanda[2]} Sushi(s) ---- R${comanda[2] * cardapio.get('Sushi'):.2f}")  
        print(f"Você pediu {comanda[3]} Temakis(s) ---- R${comanda[3] * cardapio.get('Temaki'):.2f}") 
        print("========================================")
        print(f"O valor da taxa do garçom ---- R${comanda[0]*gorjetaGarcom:.2f}")
        print("========================================")
        print(f"O preço final foi R${comanda[0]+(comanda[0]*gorjetaGarcom):.2f}")    
        print("========================================")
        break
