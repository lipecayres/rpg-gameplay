# Prototypes

import dice
import items
import level
import options
import status

# Variables:

#Game Name
game = ""  
#Player's Quantity
playerNumber = 0   
#Players Username
playerNames = []
#Player's inventory
inventory = []
# Player's Level
levelPlayer = []


def menu():

    print()
    print("################################")
    print()
    print()
    print("--------------------------------")
    print("What do you want to do now?")
    print("1- Roll the dice ")
    print("2- Manage Items")
    print("3- Level")
    print("4- See players status")
    print("5- Game Options")
    print("--------------------------------")
    print()
    print("################################")
    print()
    
    cursor = -1
    while True:
        cursor = input("Choose a number: ")
        if cursor.isdigit():
            cursor = int(cursor)
            break
        else:
            print()
            print("Insert a number!")
            print()

    if cursor == 1:
        dice.menuDice()
    elif cursor == 2:
        items.menuItems()
    elif cursor == 3:
        level.menuLevel() 
    elif cursor == 4:
        status.menuStatus() 
    elif cursor == 5:
        options.menuOptions() #pending
    else:
        print()
        print("Invalid entry. Try again")
        print()        
        intro.menu()



    # Introduction
#Starting game


def opening():
    
    print("################################")
    print("#")
    print("# RPG Game Play")
    print("#")
    print("# This game play allows you") 
    print("# to keep in track")
    print("# in your RPG Game!") 
    print("#")
    print("# Have fun!")
    print("#")
    print('# Developed by: Felipe Cayres')
    print("################################")
    print()




def intro():

    print()
    print("################################")
    print()
    print("Hi! Let's play a game?")
    print()
    print("################################")
    print()


        # Defining game name
    print("What's the game name we are playing? ")
    game = input("Game name: ")
    print()
    print("Nice! So, let's play " + game)
    print()

        # Defining Players Quantity 


    while True:
        print("How many players are playing? (Max: 6)")
        
        playerNumber = -1
        while True:
            playerNumber = input("Quantity: ")
            if playerNumber.isdigit():
                playerNumber = int(playerNumber)
                break
            else:
                print()
                print("Insert a number!")
                print()

        if playerNumber > 0 and playerNumber <= 6:
            break
        elif playerNumber < 0:
            print("At least 1 player! Try again")
        else:
            print("Max 6 players. Try again.")
    print()

        #Setting inventory and menuLevel of players    
    for i in range(playerNumber):
        
        inventory.append([])
        levelPlayer.append(0)


        # Defining players username
    print("Time to set player's name!")
    print()
    counter = 0
    for player in range(playerNumber):
        while True:
            print(f"How should we call Player {counter+1}: ")
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
    counter = 1
    for player in playerNames:
        print(f"Player {counter}: {player}")
        counter +=1
    print()
