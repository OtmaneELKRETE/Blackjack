import random

"""
Classe Carte qui gère la création du deck, le mélange des cartes, la distribution des cartes et le calcul de la valeur des cartes et des mains.
"""
class Carte:

    """
    Constructeur de la classe Carte
    """
    def __init__(self):
        self.cartes = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        self.couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        self.deck = []

    """
    Génération du deck de cartes
    """
    def GenerationDeck(self):
        for couleur in self.couleurs:
            for carte in self.cartes:
                self.deck.append(carte + " de " + couleur) 

    """
    Mélange du deck de cartes
    """
    def melange(self):
        random.shuffle(self.deck)
        return self.deck

    """
    Distribution de cartes
    """
    def distributionCarte(self, deck):
        main = []
        for i in range(2):
            main.append(deck.pop())
        return main

    """
    Calcul de la valeur d'une carte
    """
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

    """
    Calcul de la valeur d'une main pour le joueur
    """
    def valeurMainJoueur(self, main):
        valeur = 0
        asValue = 0
        
        for carte in main:
            if carte.startswith("As"):
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

    """
    Calcul de la valeur d'une main pour la banque
    """
    def valeurMainBanque(self, main):
            valeur = 0
            for carte in main:
                valeur += self.valeurCarte(carte,11)

            if valeur > 21:
                for carte in main:
                    if carte.startswith("As"):
                        valeur -= 10
            return valeur

    
