import csv

#Game Name
game = "DEDDDD"  
#Player's Quantity
playerNumber = 3   
#Players Username
playerNames = ["Pablo","mario", "jose"]
#Player's inventory
inventory = [["Espada"],["Escudo"], ["Cajado"]]
# Player's Level
levelPlayer = [0,7,3]

print(type((game)))
print(playerNumber)
print(type((playerNames)))
print(inventory)
print(levelPlayer)

print()
print("----------------------------------------")
print()


def loadGame():

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
    playerNames = list(load[0][2].split(","))
    inventory = list(load[0][3].split(","))
    levelPlayer = list(load[0][4].split(","))

    print(load)
    print(game)
    print(playerNumber)
    print(playerNames)
    print(inventory)
    print(levelPlayer)

loadGame()



print("----------------------------------------")
print("----------------------------------------")
print()
print(load)
print()



print(type((game)))
print(playerNumber)
print(type(playerNames))
print(inventory)
print(levelPlayer)






