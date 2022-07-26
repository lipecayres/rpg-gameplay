import random

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
    menu()


    # Introduction
def intro():
    print()
    print("Hi! Let's play a game?")
    print()

        # Defining game name
    print("What is the game name we are playing? ")
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
    
    print("All set! Let's start the game!")
    print()
    counter = 0
    for player in playerNames:
        print(f"Player {counter}: {player}")
        counter +=1
    print()


def menu():
    
    print("--------------------------------")
    print("What do you want to do now?")
    print("1- Roll the dice ")
    print("2- Add items")
    print("3- Remove items")
    print("4- See players status")
    print("5- End Game")
    print("--------------------------------")
    cursor = -1
    cursor = int(input("Choose a number: "))
    if cursor == 1:
        menuDice() #Pendente
    elif cursor == 2:
        itens() #pendente
    elif cursor == 3:
        level() #pendente
    elif cursor == 4:
        info() #pendente
    elif cursor == 5:
        options() #pendente
    else:
        print()
        print("Invalid entry. Try again")
        print()        
        menu()

def menuDice():
    print()
    print("--------------------------------")
    print("How many dices do we play?")
    print("1- One dice")
    print("2- Two dices")
    print("3- Return")
    print("--------------------------------")
    
    cursor = -1
    cursor = int(input("Choose a number: "))
    if cursor == 1:
        sortingDice1() 
    elif cursor == 2:
        sortingDice2() #pendente
    elif cursor == 3:
        menu() 
    else:
        print("Invalid entry. Try again")
        menuDice()

def sortingDice1():
    sortDice = random.randint(1,6) 
    print()
    print("..........Sorting dice..........")
    print()
    print("Here's the sorted number:")
    print(f"Dice: {sortDice}")
    
    menuDice()
    
def sortingDice2():
    sortDice1 = random.randint(1,6) 
    sortDice2 = random.randint(1,6)
    print()
    print("..........Sorting dices..........")
    print()
    print("Here's the sorted number:")
    print(f"Dice 1: {sortDice1}")
    print(f"Dice 2: {sortDice2}")

    menuDice()

def itens():
    #Função para apresentar os itens cadastrados ao usuário
    print()

    menu()

def level():
    #Função para mostrar o level dos usuários
    print()
    menu()

def info():
    #função para mostrar as informações dos usuários ativos
    print()
    menu()

def options():
    #Função para abrir opções do sistema
    print() 
    menu()

main()