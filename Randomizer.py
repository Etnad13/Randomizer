import random

def rand(n):
    try:
        for x in range(0,n+1):
            print(random.random())
        return
    except ValueError:
        quit()

def main():
    rand(int(input("Enter the number of random values less than 1.00 that you'd like to obtain: ")))
    return

try:
    main()
except ValueError:
    quit()