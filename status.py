import intro

####### READY - MENU STATUS PLAYER  ##############
    
    
def menuStatus():
    #Show all informations about players

    print()
    print("//////////////////////////")
    print(" Player's Status")
    print()
    for player in intro.playerNames:
        print("-----------------------")  
        print(f"Player: {player}")
        print(f"Level: {intro.levelPlayer[playerNames.index(player)]}")
        print()
        print(player + " inventory")
        for item in intro.inventory[playerNames.index(player)]:
            print("| " + item, end = " |")
        print()
        print("-----------------------")  
    print("//////////////////////////")
    print()
    print()
    intro.menu()
