# RPG Supporting System

# Variables:

#Game Name
game = ""  

#Player's Quantity
playerNumber = 0   

#Players Username
playerNames = []

# Game Cursor
cursor = 0

    # Game
def main():
    #Starting game
    intro()



    # Introduction
def intro():
    print()
    print("Hi! Let's play a game?")
    print()

        # Defining game name
    print("What is the gane name we are playing? ")
    game = input("Game name: ")
    print()
    print("Nice! So, let's play " + game)
    print()

        # Defining Players Quantity 
    while True:
        print("How many players are playing? (Max: 6)")
        playerNumber = int(input("Quantity: "))
        if playerNumber > 0 and playerNumber <= 6:
            break
        elif playerNumber < 0:
            print("At least 1 player! Try again")
        else:
            print("Max 6 players. Try again.")
    print()
        
        # Defining players username
    print("Time to ser the player's name!")
    print()
    counter = 0
    for player in range(playerNumber):
        while True:
            print(f"How should we call player {counter+1}: ")
            p = input("Name: ")
            print()
            print("Are you sure about the name? (Yes/No): " + p)
            confirm = input("Confirm?: ")
            if confirm[0].lower() == 'y':
                playerNames.append(p)
                counter +=1
                break 
    print(playerNames)

print("All set! Let's start the game!")
print()

def menu():
    print("What do you want to do now?")
    print("1- Roll the dice ")
    print("2- Manage items")
    print("3- Level")
    print("4- See informations")
    print("5- Game Options")
    cursor = input("Choose a number: ")
    if cursor == "1":
        dice() #Pendente
    if cursor == "2":
        itens() #pendente
    if cursor == "3":
        level() #pendente
    if cursor == "4":
        info() #pendente
    if cursor == "5":
        options() #pendente

def dice():
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

def options():
    #Função para abrir opções do sistema
    print() 
    
main()