def main():
    n = int(input("How many meows?: "))
    meow(n)

def meow(n):
    for i in range(n):
        print("meow!")

main()