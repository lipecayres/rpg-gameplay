import random

def sortingDice1():
    cursor = 0
    while True:
        sortDice1 = random.randint(1,6) 
        print("Sorting dice...")
        print()
        print(f"Here's the sorted number: {sortDice1}")
        print()
        print("What to do now?")
        print()
        print("1. Roll the dice again")
        print("2. Return")
        cursor = int(input("Choose a number: "))
        if cursor == 1:
            return True
        if cursor == 2:               
            return False
        else:
            print("Invalid entry. Try again!")
            return False

sortingDice1()