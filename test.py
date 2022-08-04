import pandas as pd

# Variables:

#Game Name
game = "DED"  
#Player's Quantity
playerNumber = 3   
#Players Username
playerNames = ["LiipeC", "Vraus"]
#Player's inventory
inventory = [["Espada", "Escudo"], ["Arma", "Fire"]]
# Player's Level
levelPlayer = [3,5]


def saveGame():

    dict = {
    "game": game,
    "playerNumber": playerNumber,
    "playerNames": playerNames,
    "inventory": inventory,
    "levelPlayer": levelPlayer
    }


    print("ATTENTION! Same name -> Overwrite!")
    savefile = input("FILE NAME: ")
    
    dict = pd.DataFrame(dict)

    print(dict)
 
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

saveGame()