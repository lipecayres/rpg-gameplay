import random
import intro


############ READY - MENU DICE ###################

def menuDice():
    print()
    print("--------------------------------")
    print("How many dices do we play?")
    print("1- One dice")
    print("2- Two dices")
    print("3- Return")
    print("--------------------------------")


    cursor = intro.intEntry()
    if cursor == 1:
        sortingDice1() 
    elif cursor == 2:
        sortingDice2()
    elif cursor == 3:
        intro.menu() 
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
