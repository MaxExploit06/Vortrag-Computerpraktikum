import random

def coin_toss():
    return "K" if random.randint(0,1) else "Z"

def main():
    n = int(input("Wie viele Wiederholungen möchten Sie?\n"))
    Kopf = 0
    Zahl = 0
    for i in range (0, n):
        Ergebniss = coin_toss()
        if (Ergebniss == "K"):
            Kopf += 1
        else:
            Zahl += 1

    Betrag = (10 * Kopf) - (10 * Zahl)

    print (f"Die Münze wurde {n} mal geworfen. Kopf wurde {Kopf} mal gezeigt und Zahl wurde {Zahl} mal.")
    if (Betrag < 0):
        print ("Ihr Verlust:", abs(Betrag), "Euro")
    else:
        print ("Ihr Gewinn:", Betrag, "Euro")

    # print(Ergebnisse)
    return

main()