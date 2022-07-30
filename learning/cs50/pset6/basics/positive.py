def positive():
    while True:
        n = int(input("N: "))
        if n > 0:
            break
    return n

positive()