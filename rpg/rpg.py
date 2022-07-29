
##########################
#
# RPG Game Play
#
##########################

#Prototypes
import random
import csv


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

#
### MAIN GAME 
#

def main():

    #Starting game
    
    opening()
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
        menuDice()
    elif cursor == 2:
        menuItems()
    elif cursor == 3:
        menuLevel() 
    elif cursor == 4:
        menuStatus() 
    elif cursor == 5:
        menuOptions() #pending
    else:
        print()
        print("Invalid entry. Try again")
        print()        
        menu()


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
    print(" Itens menuOptions")
    print("1- Add inventory ")
    print("2- Remove inventory")
    print("3- Return")
    print("//////////////////////////")
    print()

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

    #Function to show the level menu menuOptions to the user
    print()
    print(" ~~ All Player's Level: ")
    print()
    for player in playerNames:
        print(f"Player: {player}")
        print(f"Level: {levelPlayer[playerNames.index(player)]}")
        print("-----------------------")   
    print()
    print("//////////////////////////")
    print(" Level Options")
    print("1- Upgrade level ")
    print("2- Decrease level")
    print("3- Return")
    print("//////////////////////////")
    print()

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
            if newLevel.isdigit():
                newLevel = int(newLevel)
                break
            else:
                print()
                print("Insert a number!")
                print()
 
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
           if newLevel.isdigit():
               newLevel = int(newLevel)
               break
               
           else:
               print()
               print("Insert a number!")
               print()

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


##################################################
##################################################
##################################################


####### READY - MENU STATUS PLAYER  ##############
    
    
def menuStatus():
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


##################################################
##################################################
##################################################


####### HAVE TO FIX!!! - MENU STATUS PLAYER  ##############


def menuOptions():
    #Função para abrir opções do sistema  


    print("//////////////////////////")
    print(" ~~ Game Options")
    print()
    print("1- Save Game ")
    print("2- Load Game")
    print("3- Reset Game")
    print("4- Return")
    print("//////////////////////////")
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
        print()
        saveGame() #pendente 

    elif cursor == 2:
        print()
        loadGame() #pendente 

    elif cursor == 3:
        print()
        resetGame() #pendente
       
    elif cursor == 4:
        print()
        menu()

    else:
        print()
        print("Invalid entry. Try again")
        print()        
        menuOptions()

def saveGame():

    print(" WOrking on it...")

    menuOptions()

    print("ATTENTION! Same name -> Overwrite!")
    savefile = input("FILE NAME: ")
    with open(savefile + ".csv", "w", encoding = "UTF8", newline = "\n") as file:
        writer = csv.writer(file)
        writer.writerow([game])
        writer.writerow([playerNumber])
        writer.writerow([playerNames])
        writer.writerow([inventory])
        writer.writerow([levelPlayer])

    print("Game saved as:  " + savefile)
    menuOptions()

def loadGame():
    
    print(" WOrking on it...")

    menuOptions()

    global load    
    load = []

    print("Let's load your game!")
    loading = input("FILE NAME: ")     
    with open(loading + ".csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            load.append(row)

    global game 
    global playerNumber
    global playerNames
    global inventory 
    global levelPlayer

    game = load[0][0]
    playerNumber = load[0][1]
    playerNames = load[0][2]
    inventory = load[0][3]
    levelPlayer = load[0][4]

    print()
    print("###########################")
    print("GAME " + loading + " LOADED!")
    print("###########################")
    print()
    menu()

def resetGame():
    
    global game, playerNumber, playerNames, inventory, levelPlayer
    
    print("Are you sure about it?")
    print("All your progress will be loss")    
    print()
    confirm = input("Confirm? (Yes/No): ")
    if confirm[0].lower() == 'y':
        game = ""  
        playerNumber = 0   
        playerNames = []
        inventory = []
        levelPlayer = []
       
        intro()

    else:
        print()
        print("Invalid entry. Try again!")
        print()
        menuOptions()










main()