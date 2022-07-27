import random

#
# RPG Game Play
#

# Variables:

#Game Name
game = ""  
#Player's Quantity
playerNumber = 0   
#Players Username
playerNames = []
# Game Cursor
cursor = 0
#Player's inventory
inventory = []
# Player's Level
levelPlayer = []

#
### MAIN GAME 
#

def main():

    #Starting game

    intro()  
    menu()


def menu():
    
    print("--------------------------------")
    print("What do you want to do now?")
    print("1- Roll the dice ")
    print("2- Manage Items")
    print("3- Level")
    print("4- See players status")
    print("5- Game Options")
    print("--------------------------------")
    cursor = -1
    cursor = int(input("Choose a number: "))
    if cursor == 1:
        menuDice()
    elif cursor == 2:
        menuItems()
    elif cursor == 3:
        menuLevel() 
    elif cursor == 4:
        menuInfo() #pendente
    elif cursor == 5:
        options() #pendente
    else:
        print()
        print("Invalid entry. Try again")
        print()        
        menu()


    
    
def menuInfo():
    #Show all informations about players

    print()
    print("//////////////////////////")
    print(" Player's Status")
    print()
    for player in playerNames:
        print("-----------------------")  
        print(f"Player: {player}")
        print(f"Level: {levelPlayer[playerNames.index(player)]}")
        print()
        print(player + " inventory")
        for item in inventory[playerNames.index(player)]:
            print("| " + item, end = " |")
        print()
        print("-----------------------")  
    print("//////////////////////////")
    print()
    print()
    menu()

def options():
    #Função para abrir opções do sistema
    print() 
    menu()


##################################################
##################################################
##################################################


########### READY - INTRO GAME  ##################

    # Introduction

def intro():
    print()
    print("Hi! Let's play a game?")
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
        playerNumber = int(input("Quantity: "))
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

##################################################
##################################################
##################################################

############ READY - MENU DICE ###################

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
        sortingDice2()
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

##################################################
##################################################
##################################################

########## READY - MENU MANAGE ITEMS  ####################

# Menu : 2. Manage Items

def menuItems():
    # This function show informations about player's inventory
    
    print()
    print("//////////////////////////")
    print(" Itens options")
    print("1- Add inventory ")
    print("2- Remove inventory")
    print("3- Return")
    print("//////////////////////////")
    print()

    cursor = -1
    cursor = int(input("Choose a number: "))
    if cursor == 1:
        print()
        addItems() 
    elif cursor == 2:
        print()
        removeItems() 
    elif cursor == 3:
        print()
        menu()
    else:
        print()
        print("Invalid entry. Try again")
        print()        
        menuItems()


# Menu inventory: 2.1 Add inventory
# Add inventory function

def addItems():
    print()
    print("Ok, Let's add some inventory. What player should we add an item?")
    print()
    print("Player's")
    for player in playerNames:
        print("| " + player, end = " |")
    print()
    print()
    player = input("Player name: ")
    if player in playerNames:
           
           # Asking the item name

           print()
           print("Which item are we adding?")
           for item in inventory[playerNames.index(player)]:
               print("| " + item, end = " |")
           print()
           print()
           addItemName = input("Item name: ")
           print()
           print("Are you sure about the item name? (Yes/No): " + addItemName)
           confirm = input("Confirm?: ")

           # Adding item to player 

           if confirm[0].lower() == 'y':
               inventory[playerNames.index(player)].append(addItemName)
               print("Item saved! What do you want to do now?")
               print()
               print(player + " complete inventory")
               for item in inventory[playerNames.index(player)]:
                   print("| " + item, end = " |")
               print()
               print()
               print("1. Add another item")
               print("2. Return")
               cursor = -1
               cursor = int(input("Choose a number: "))
               if cursor == 1:
                   addItems()
               elif cursor == 2:
                   menuItems()
               else:
                    print()
                    print("Invalid entry! Try again.")
                    print()
                    addItems()
           
           elif confirm[0].lower() == "n":
               print()
               print("Item not added! ")

               menuItems()

           else:
               print()
               print("Invalid entry! Try again.")
               print()
               menuItems()    
    else:
        print()
        print("Player not found. What to do now?")
        print()
        menuItems()


# Menu inventory: 2.1 Remove inventory
# Remove inventory function

def removeItems():

    print()
    print("Ohh, OK! Time to remove inventory! What player should we remove an item?")
    print()
    print("Player's")
    for player in playerNames:
        print("| " + player, end = " |")
    print()
    print()
    player = input("Player name: ")
    if player in playerNames:
           
           # Asking the item name

           print()
           print("Which item are we removing?")
           print()
           print(player + " complete inventory")
           for item in inventory[playerNames.index(player)]:
               print("| " + item, end = " |")
           print()
           print()
           removeItemName = input("Item name: ")
           print()
           print("Are you sure about the item name? (Yes/No): " + removeItemName)
           confirm = input("Confirm?: ")

           # Removing item to player 

           if confirm[0].lower() == 'y':
               if removeItemName in inventory[playerNames.index(player)]:
                   inventory[playerNames.index(player)].remove(removeItemName)
                   print()
                   print("Item removed! What do you want to do now?")
                   print()
                   print(player + " complete inventory")
                   for item in inventory[playerNames.index(player)]:
                       print("| " + item, end = " |")
                   print()
                   print()
                   print("1. Remove another item")
                   print("2. Return")
                   cursor = -1
                   cursor = int(input("Choose a number: "))
                   if cursor == 1:
                       removeItems()
                   elif cursor == 2:
                       menuItems()
                   else:
                       print()
                       print("Invalid entry! Try again.")
                       print()
                       menuItems()

               else:
                print()
                print("Item does not exist at inventory.")
                print()
                removeItems()     
           
           elif confirm[0].lower() == "n":
               print()
               print("Item not removed! Try again. ")

               menuItems()

           else:
               print()
               print("Invalid entry! Try again.")
               print()
               menuItems()    
    else:
        print()
        print("Player not found. What to do now?")
        print()
        menuItems()

##################################################
##################################################
##################################################

########## READY - MENU LEVEL  ####################

def menuLevel():

    #Function to show the level menu options to the user
    print()
    print(" ~~ All Player's Level: ")
    print()
    for player in playerNames:
        print(f"Player: {player}")
        print(f"Level: {levelPlayer[playerNames.index(player)]}")
        print("-----------------------")   
    print()
    print("//////////////////////////")
    print(" Level options")
    print("1- Upgrade level ")
    print("2- Decrease level")
    print("3- Return")
    print("//////////////////////////")
    print()

    cursor = -1
    cursor = int(input("Choose a number: "))
    if cursor == 1:
        print()
        addLevel() 

    elif cursor == 2:
        print()
        removeLevel() 

    elif cursor == 3:
        print()
        menu()
    else:
        print()
        print("Invalid entry. Try again")
        print()        
        menuLevel()

# Adding level to a player
def addLevel():

    print()
    print("Nice! What player should we upgrade?")
    print()
    print(" ~~ Player's:")
    for player in playerNames:
        print("| " + player, end = " |")
    print()
    print()
    player = input("Player name: ")
    if player in playerNames:

           # Adding level to a player 
        
        print()
        print("==========================")
        print("====== UPGRADE BOX =======")
        print(f"Player: {player}")
        print(f"Actual Level: {levelPlayer[playerNames.index(player)]}")
        print("==========================")           

            # Asking for the new level of the choosed player
        while True:
            newLevel = input("New level: ")
            if (newLevel.isalpha()) == True:
                print()
                print("Insert a number!")
                print()
            else:
                break
        print()
        print(f"Are you sure about the new level? (Yes/No): {newLevel}")
        confirm = input("Confirm?: ")

        if confirm[0].lower() == 'y':
            print()
            levelPlayer[playerNames.index(player)] = newLevel
            
            # Returning message: Level added ok!            
            print("All set! What do you want to do now?")
            menuLevel()
        
        else:
            print()
            print("Invalid entry. Try again!")
            print()
            menuLevel()

    # Error message
    else:
        print()
        print("Player not found. What to do now?")
        print()
        menuLevel()


# Removing level from a player
def removeLevel():

    
    print()
    print("Ohh! What player should we decrease level?")
    print()
    print(" ~~ Player's:")
    for player in playerNames:
        print("| " + player, end = " |")
    print()
    print()
    player = input("Player name: ")
    if player in playerNames:

           # Adding level to a player 

        print("==========================")
        print("====== DECREASE BOX =======")
        print()
        print(f"Player: {player}")
        print(f"Actual Level: {levelPlayer[playerNames.index(player)]}")

        print("==========================")           

            # Asking for the new level of the choosed player
        while True:
            newLevel = input("New level: ")
            if (newLevel.isalpha()) == True:
                print()
                print("Insert a number!")
                print()
            else:
                break
        print()
        print(f"Are you sure about the new level? (Yes/No): {newLevel}")
        confirm = input("Confirm?: ")

        if confirm[0].lower() == 'y':
            print()
            levelPlayer[playerNames.index(player)] = newLevel
            
            # Returning message: Level added ok!            
            print("All set! What do you want to do now?")
            menuLevel()
        
        else:
            print()
            print("Invalid entry. Try again!")
            print()
            menuLevel()

    # Error message
    else:
        print()
        print("Player not found. What to do now?")
        print()
        menuLevel()    








main()