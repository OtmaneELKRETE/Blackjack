import Carte

"""
Joueur pour le jeu de Blackjack
"""
class Joueur:
    def __init__(self, nom,argent):
        self.nom = nom
        self.argent = argent

    def GestionJoueuréponse(self, main, deck):
        choix=False
        while choix==False and len(main)<=21:
            reponse = input("Voulez-vous tirer une carte ? (oui/non) : ")
            if reponse == "oui":
                main.append(deck.deck.pop())
                valeur = deck.valeurMain(main)
                print("Votre main :", main, "Valeur :", valeur)
            elif reponse == "non":
                choix=True