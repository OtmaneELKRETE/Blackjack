import random

def main():
    print("Bienvenue dans le jeu de Blackjack !")
    deck = JeuDeCarte()
    deck = melange(deck)
    main = distributionCarte(deck)
    banque = distributionCarte(deck)
    print("Votre main :", main)
    print("Main de la banque :", banque)

    GestionJoueuréponse(main,deck)
    GestionBanqueRéponse(banque,deck)


def JeuDeCarte():
    carte = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
    couleur = ["Coeur", "Carreau", "Trèfle", "Pique"]
    deck = []

    for c in couleur :
        for ca in carte :
            deck.append(ca + " de " + c)
    return deck

def melange(deck):
    random.shuffle(deck)
    return deck

def distributionCarte(deck):
    main = []
    for i in range(2):
        main.append(deck.pop())
    return main


def GestionJoueuréponse(main,deck):
    choix=False
    while choix==False:
        reponse = input("Voulez-vous tirer une carte ? (oui/non) : ")
        if reponse == "oui":
            main.append(deck.pop())
            print("Votre main :", main)

def GestionBanqueRéponse(banque,deck):
    choix=False
    while choix==False:
        if len(banque)<17:
            banque.append(deck.pop())
            print("Main de la banque :", banque)


print(main())