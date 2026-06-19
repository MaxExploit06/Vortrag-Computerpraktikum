import random

#global variables
balance = int(input("Mit wie viel Geld wollen Sie anfangen?: "))
main_deck = [
    "K7", "K8", "K9", "K10", "KB", "KD", "KK", "KA",
    "P7", "P8", "P9", "P10", "PB", "PD", "PK", "PA",
    "H7", "H8", "H9", "H10", "HB", "HD", "HK", "HA",
    "C7", "C8", "C9", "C10", "CB", "CD", "CK", "CA"
]

def main():






    choice = input("Noch eine Runde? [J/N]: ").lower()
    if choice == "n":
        #TODO: show money left
        quit()
    else:
        main()


#Starting the simulation
print("")

main()
