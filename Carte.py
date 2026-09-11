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