# Get Height from the user

while True:
    n = int(input("Height: "))
    if (n > 0 and n <=8):
        break

# Printing image

for i in range(n):
    print((n - 1 - i) * " ", end = "")
    print((i+1) * "#")