########## READY - MENU LEVEL  ####################
# Add level
# Remove level

import intro

def menuLevel():

    #Function to show the level menu menuOptions to the user
    print()
    print(" ~~ All Player's Level: ")
    print()
    for player in intro.playerNames:
        print(f"Player: {player}")
        print(f"Level: {intro.levelPlayer[playerNames.index(player)]}")
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
        intro.menu()
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
    for player in intro.playerNames:
        print("| " + player, end = " |")
    print()
    print()
    player = input("Player name: ")
    if player in intro.playerNames:

           # Adding level to a player 
        
        print()
        print("==========================")
        print("====== UPGRADE BOX =======")
        print(f"Player: {player}")
        print(f"Actual Level: {intro.levelPlayer[playerNames.index(player)]}")
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
            intro.levelPlayer[playerNames.index(player)] = newLevel
            
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
    for player in intro.playerNames:
        print("| " + player, end = " |")
    print()
    print()
    player = input("Player name: ")
    if player in intro.playerNames:

           # Adding level to a player 

        print("==========================")
        print("====== DECREASE BOX =======")
        print()
        print(f"Player: {player}")
        print(f"Actual Level: {intro.levelPlayer[playerNames.index(player)]}")

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
            intro.levelPlayer[playerNames.index(player)] = newLevel
            
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
