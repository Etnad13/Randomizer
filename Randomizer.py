import random

def rand(n):
    try:
        for x in range(n+1):
            print(random.random())
        return
    except ValueError:
        quit()

def randInt(n):
    try:
        dice = random.randint(1,n)
        return dice
    except ValueError:
        quit()


def main():
    print(randInt(int(input("Enter the amount of sides for the dice you would like to use:"))))
    rand(int(input("Enter the number of random values less than 1.00 that you'd like to obtain: ")))
    return

try:
    main()
except ValueError:
    quit()