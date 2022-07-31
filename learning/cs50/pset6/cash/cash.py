# Asking an owe to the user:

while True:
    n = float(input("Change owed: "))
    if n >= 0:
        break

# Coins available

coins = [25, 10, 5, 1]

# Counter and total coins
owe = round(n*100)
counter = 0

# Checking coins quantity

while owe >= coins[0]:
    owe -=coins[0]
    counter += 1

while owe >= coins[1]:
    owe -=coins[1]
    counter += 1

while owe >= coins[2]:
    owe -=coins[2]
    counter += 1

while owe >= coins[3]:
    owe -=coins[3]
    counter += 1

print(counter)