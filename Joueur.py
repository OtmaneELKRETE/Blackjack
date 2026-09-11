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
                valeurJeu = deck.valeurMainJoueur(main)
                print("Votre main :", main, "Valeur :", valeurJeu)
            elif reponse == "non":
                choix=True

        return valeurJeu, main

    def gestionComportementEnFonctionMainJoueur(self, valeurJeu, mainjoueur):
            res = False
    
            if valeurJeu > 21:
                print("Vous avez dépassé 21. Vous avez perdu !")
            elif valeurJeu == 21 and len(mainjoueur) == 2:
                print("Blackjack ! Vous avez gagné !")
            else:
                res = True
    
            return res