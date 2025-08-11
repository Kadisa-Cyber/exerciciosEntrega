""" 
Feito na aula de Projeto Back-End
Kauan Dias Santos
"""

import os
os.system('cls')

def verificar_disponilidade(reservas, salas, salaOpcao, horarios, horarioOpcao):
    salaDisponivel = True
    salaEscolhida = salas[salaOpcao-1]
    horarioEscolhido = horarios[horarioOpcao-1]

    if (salaEscolhida, horarioEscolhido) in reservas:
        salaDisponivel = False

    if salaDisponivel == False:
        return("Sala indisponivel!")
    else:
        return("Sala disponivel!")


reservas = [("Sala 1", "10h"), ("Sala 2", "11h30"), ("Sala 3", "15h")]
salasDisponiveis = ["Sala 1", "Sala 2", "Sala 3"]
horariosDisponiveis = ["10h", "11h30", "12h", "13h30", "15h", "16h30", "18h"]

sair = False

while not sair:

    opcaoUsuario = int(input("O que você deseja? \n 1. Adicionar reservas \n 2. Verificar horários \n Resposta: "))
       
    if opcaoUsuario == 1:

        for i, sala in enumerate(salasDisponiveis): 
            print(f"{i+1} - {sala}")
        opcaoSala = int(input("Qual das salas você deseja reservar?: ")) 
        for i, horario in enumerate(horariosDisponiveis):
            print(f"{i+1} - {horario}")
        opcaoHorario = int(input("Qual horário você deseja?(Ex: 14h): "))  

        if verificar_disponilidade(reservas, salasDisponiveis, opcaoSala, horariosDisponiveis, opcaoHorario) == "Sala disponivel!":
            reservas.append((salasDisponiveis[opcaoSala-1], horariosDisponiveis[opcaoHorario-1]))
            print("========================================")
            print("Horário reservado com sucesso!")
            print("========================================")
        else:
            print("========================================")
            print("A sala nesse horário já está ocupada")
            print("========================================")
            
    elif opcaoUsuario == 2:

        for i, sala in enumerate(salasDisponiveis): 
            print(f"{i+1} - {sala}")
        opcaoSala = int(input("Qual das salas você deseja reservar? ")) 
        for i, horario in enumerate(horariosDisponiveis):
            print(f"{i+1} - {horario}")
        opcaoHorario = int(input("Qual horário você deseja?(Ex: 14h): "))  

        print("========================================")
        print(verificar_disponilidade(reservas, salasDisponiveis, opcaoSala, horariosDisponiveis, opcaoHorario))
        print("========================================")

    opcSair = int(input("Você deseja sair? \n 1. Não \n 2. Sim \n Resposta: "))
    if opcSair == 2:
        sair = True  
        break

    os.system('cls')

print(reservas)
