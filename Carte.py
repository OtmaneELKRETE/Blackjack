import random


class Carte:
    def __init__(self):
        self.cartes = ["As","5", "6", "7", "8", "9","Dame", "Roi"]
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

    def valeurCarte(self, carte, asValue):
        res = 0
        if carte.startswith("As"):
            res = asValue
        elif carte.startswith("2"):
            res = 2
        elif carte.startswith("3"):
            res = 3
        elif carte.startswith("4"):
            res = 4
        elif carte.startswith("5"):
            res = 5
        elif carte.startswith("6"):
            res = 6
        elif carte.startswith("7"):
            res = 7
        elif carte.startswith("8"):
            res = 8
        elif carte.startswith("9"):
            res = 9
        else:
            res = 10
        return res

    def valeurMainJoueur(self, main):
        valeur = 0
        asValue = 0
        
        for carte in main:
            if carte == "As":
                try:
                    res = int(input("Voulez-vous que l'As vaille 1 ou 11 ? (1/11) : "))
                    if res == 11:
                        asValue = 11
                    else:
                        asValue = 1
                except ValueError:
                    print("Entrée invalide. L'As vaudra 1 par défaut.")

            valeur += self.valeurCarte(carte,asValue)     
        return valeur

    def valeurMainBanque(self, main):
            valeur = 0
            for carte in main:
                valeur += self.valeurCarte(carte,11)

            if valeur > 21:
                for carte in main:
                    if carte.startswith("As"):
                        valeur -= 10
            return valeur

    
