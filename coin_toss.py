import random

def coin_toss():
    return "K" if random.randint(0,1) else "Z"

def main():
    n = int(input("Wie viele Wiederholungen möchten Sie?\n"))
    heads = 0
    tails = 0
    for i in range (0, n):
        result = coin_toss()
        if (result == "K"):
            heads += 1
        else:
            tails += 1

    amount = (10 * heads) - (10 * tails)

    print (f"Die Münze wurde {n} mal geworfen. Kopf wurde {heads} mal gezeigt und Zahl wurde {tails} mal.")
    if (amount < 0):
        print ("Ihr Verlust:", abs(amount), "Euro")
    else:
        print ("Ihr Gewinn:", amount, "Euro")

    return

main()
