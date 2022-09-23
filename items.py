# Menu : 2. Manage Items
# Add item
# Remove item

import intro

def menuItems():
    # This function show informations about player's inventory
    
    print()
    print("//////////////////////////")
    print(" Itens Options")
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
        intro.menu()
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
    for player in intro.playerNames:
        print("| " + player, end = " |")
    print()
    print()
    player = input("Player name: ")
    if player in intro.playerNames:
           
           # Asking the item name

           print()
           print("Which item are we adding?")
           for item in intro.inventory[intro.playerNames.index(player)]:
               print("| " + item, end = " |")
           print()
           print()
           addItemName = input("Item name: ")
           print()
           print("Are you sure about the item name? (Yes/No): " + addItemName)
           confirm = input("Confirm?: ")

           # Adding item to player 

           if confirm[0].lower() == 'y':
               intro.inventory[intro.playerNames.index(player)].append(addItemName)
               print("Item saved! What do you want to do now?")
               print()
               print(player + " complete inventory")
               for item in intro.inventory[intro.playerNames.index(player)]:
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
    for player in intro.playerNames:
        print("| " + player, end = " |")
    print()
    print()
    player = input("Player name: ")
    if player in intro.playerNames:
           
           # Asking the item name

           print()
           print("Which item are we removing?")
           print()
           print(player + " complete inventory")
           for item in intro.inventory[intro.playerNames.index(player)]:
               print("| " + item, end = " |")
           print()
           print()
           removeItemName = input("Item name: ")
           print() 
           print("Are you sure about the item name? (Yes/No): " + removeItemName)
           confirm = input("Confirm?: ")

           # Removing item to player 

           if confirm[0].lower() == 'y':
               if removeItemName in intro.inventory[intro.playerNames.index(player)]:
                   intro.inventory[intro.playerNames.index(player)].remove(removeItemName)
                   print()
                   print("Item removed! What do you want to do now?")
                   print()
                   print(player + " complete inventory")
                   for item in intro.inventory[intro.playerNames.index(player)]:
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
