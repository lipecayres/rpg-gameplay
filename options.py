import csv
import intro

####### HAVE TO FIX!!! - MENU STATUS PLAYER  ##############
# Save
# Load
# Reset

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
        intro.menu()

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
        intro.game = ""  
        intro.playerNumber = 0   
        intro.playerNames = []
        intro.inventory = []
        intro.levelPlayer = []
       
        intro.intro()

    else:
        print()
        print("Invalid entry. Try again!")
        print()
        menuOptions()
