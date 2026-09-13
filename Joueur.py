import Carte

"""
Joueur pour le jeu de Blackjack
"""
class Joueur:

    """
    Constructeur de la classe Joueur
    """
    def __init__(self, nom,argent):
        self.nom = nom
        self.argent = argent

    """
    Gestion de la réponse du joueur
    """
    def GestionJoueuréponse(self, main, deck, valeurJeu):
        choix=False
        
        while choix==False and valeurJeu<21:
            reponse = input("Voulez-vous tirer une carte ? (oui/non) : ").lower()
            if reponse == "oui":
                main.append(deck.deck.pop())
                valeurJeu = deck.valeurMainJoueur(main)
                print("Votre main :", main, "Valeur :", valeurJeu)
            elif reponse == "non":
                choix=True

        return valeurJeu, main

    """
    Gestion du comportement en fonction de la main du joueur
    """
    def gestionComportementEnFonctionMainJoueur(self, valeurJeu, mainjoueur, montant, soldeBanque):
            res = False
    
            if valeurJeu == 21 and len(mainjoueur) == 2:
                print("Blackjack ! Vous avez gagné !")
                self.argent += 2.5 * montant
                soldeBanque -= 2.5 * montant
            else:
                res = True
                
            return res

    """
    Gestion de la mise du joueur
    """
    def mise(self):

        res = False
        try:
            montant = int(input("Combien voulez-vous miser ? "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")
        
        if montant <= self.argent:
            self.argent -= montant
            res = True

        return res, montant