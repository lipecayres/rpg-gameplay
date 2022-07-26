# RPG Supporting System

# Variaveis:

#Nome do jogo
game = ""  

#Quantidade de jogadores
playerNumber = 0   

#Lista de players
playerNames = []

# cursor do jogo
cursor = 0

    # game
def main():
    #inicio do jogo
    intro()



    # introdução
def intro():
    print()
    print("Olá! Vamos jogar um jogo?")
    print()

        # Nome do jogo
    print("Qual jogo estamos jogando? ")
    game = input("Nome do jogo: ")
    print()
    print("Legal, então vamos jogar " + game)
    print()

        # Personagens
    while True:
        print("Qual a quantidade de jogadores? (Max: 6)")
        playerNumber = int(input("Quantidade: "))
        if playerNumber > 0 and playerNumber <= 6:
            break
        elif playerNumber < 0:
            print("Pelo menos 1 jogador! Tente de novo")
        else:
            print("No máximo 6 jogadores. Tente de novo.")
    print()
        
        # Nome dos personagens
    print("Hora de definir o nome dos personagens!")
    print()
    counter = 0
    for player in range(playerNumber):
        while True:
            print(f"Qual o nome do personagem {counter+1}: ")
            p = input("Digite o nome: ")
            print()
            print("Confirma o nome? (Sim/Nao): " + p)
            confirm = input("Confirma?: ")
            if confirm[0].lower() == 's':
                playerNames.append(p)
                counter +=1
                break 
    print(playerNames)

print("Tudo pronto, podemos iniciar o jogo!")
print()

def menu():
    print("O que você deseja fazer agora?")
    print("1- Lançar os dados")
    print("2- Gerenciar itens")
    print("3- Level")
    print("4- Ver informações")
    print("5- Opções do jogo")
    cursor = input("Digite a opção: ")
    if cursor == "1":
        dados() #Pendente
    if cursor == "2":
        itens() #pendente
    if cursor == "3":
        level() #pendente
    if cursor == "4":
        info() #pendente
    if cursor == "5":
        opcoes() #pendente

def dados():
    #Função para jogar os dados no jogo
    print()

def itens():
    #Função para apresentar os itens cadastrados ao usuário
    print()

def level():
    #Função para mostrar o level dos usuários
    print()

def info():
    #função para mostrar as informações dos usuários ativos
    print()

def opções():
    #Função para abrir opções do sistema
    print() 
    
main()