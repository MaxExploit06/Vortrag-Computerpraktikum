import random

#Global variables
player_balance = int(input("\nMit wie viel Geld wollen Sie anfangen?: "))

def main():
    global player_balance

    player_cards = input("Karten, die Sie kaufen möchten (1€ pro Karte) : ").split()

    player_balance -= len(player_cards)

    house_cards = [
    "K7", "K8", "K9", "K10", "KB", "KD", "KK", "KA",        #Kreuz
    "P7", "P8", "P9", "P10", "PB", "PD", "PK", "PA",        #Pik
    "H7", "H8", "H9", "H10", "HB", "HD", "HK", "HA",        #Herz
    "C7", "C8", "C9", "C10", "CB", "CD", "CK", "CA"         #Karo
    ]

    random.shuffle(house_cards)

    first_pair = [house_cards[0], house_cards[1]]
    second_pair = [house_cards[2], house_cards[3]]
    third_pair = [house_cards[4], house_cards[5]]
    fourth_pair = [house_cards[6], house_cards[7]]
    big_lot = [house_cards[8]]

    payout = 0

    for i in player_cards:
        if i in first_pair:
            payout += 1
        elif i in second_pair:
            payout += 2
        elif i in third_pair:
            payout += 3
        elif i in fourth_pair:
            payout += 4
        elif i in big_lot:
            payout += 9

    player_balance += payout

    amount = payout - len(player_cards)

    print("Die folgenden Karten wurden gezogen:")
    print(f"1. Paar: {first_pair}")
    print(f"2. Paar: {second_pair}")
    print(f"3. Paar: {third_pair}")
    print(f"4. Paar: {fourth_pair}")
    print(f"großes Los: {big_lot}")
    print()
    if amount < 0:
        print("Ihr Verlust:", abs(amount), "Euro")
    else:
        print("Ihr Gewinn:", amount, "Euro")
    print("Ihr Saldo:", player_balance, "Euro")


    choice = input("Noch eine Runde? [J/N]: ").lower()
    if choice == "n":
        quit()
    else:
        main()


#Starting the simulation
print("Mit den folgenden Karten wird gespielt:")
print('''
    "K7", "K8", "K9", "K10", "KB", "KD", "KK", "KA",
    "P7", "P8", "P9", "P10", "PB", "PD", "PK", "PA",
    "H7", "H8", "H9", "H10", "HB", "HD", "HK", "HA",
    "C7", "C8", "C9", "C10", "CB", "CD", "CK", "CA"
''')

main()
