import Carte

"""
Joueur pour le jeu de Blackjack
"""
class Joueur:
    def __init__(self, nom,argent):
        self.nom = nom
        self.argent = argent

    def GestionJoueuréponse(self, main, deck, valeurJeu):
        choix=False
        while choix==False and valeurJeu<21:
            reponse = input("Voulez-vous tirer une carte ? (oui/non) : ")
            if reponse == "oui":
                main.append(deck.deck.pop())
                valeurJeu = deck.valeurMain(main)
                print("Votre main :", main, "Valeur :", valeurJeu)
            elif reponse == "non":
                choix=True

        return valeurJeu