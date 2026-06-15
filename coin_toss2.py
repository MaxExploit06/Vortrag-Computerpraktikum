import random

def coin_toss():
    return "K" if random.randint(0,1) else "Z"

def main():
    n = int(input("Wie viele Wiederholungen möchten Sie?\n"))
    print()
    for i in range (0, n):
        if (coin_toss() == "K"):
            print("■ ", end="")
        else:
            print("□ ", end="")
    print()
    print()
    return

main()