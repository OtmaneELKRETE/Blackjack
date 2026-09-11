import random


class Carte:
    def __init__(self):
        self.cartes = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        self.couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        self.deck = []

    
    def GenerationDeck(self):
        for couleur in self.couleurs:
            for carte in self.cartes:
                self.deck.append(carte + " de " + couleur) 

    def melange(self):
        random.shuffle(self.deck)
        return self.deck

    def distributionCarte(self, deck):
        main = []
        for i in range(2):
            main.append(deck.pop())
        return main

    def valeurCarte(self, carte):
        if carte.startswith("As"):
            return 1
        elif carte.startswith("2"):
            return 2
        elif carte.startswith("3"):
            return 3
        elif carte.startswith("4"):
            return 4
        elif carte.startswith("5"):
            return 5
        elif carte.startswith("6"):
            return 6
        elif carte.startswith("7"):
            return 7
        elif carte.startswith("8"):
            return 8
        elif carte.startswith("9"):
            return 9
        else:
            return 10

    def valeurMain(self, main):
        valeur = 0
        for carte in main:
            valeur += self.valeurCarte(carte)
        return valeur

