"""
Classe Banque qui gère le comportement de la banque dans le jeu de Blackjack.
"""
class Banque:

    """
    Constructeur de la classe Banque
    """
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

    """
    Gestion de la réponse de la banque
    """
    def GestionBanqueRéponse(self, banque, deck, valeurjeu):
        choix=False
        while choix==False:
            if valeurjeu<17:
                banque.append(deck.deck.pop())
                valeurjeu = deck.valeurMainBanque(banque)
                print("Main de la banque :", banque, "Valeur :", valeurjeu)
            else:
                choix=True

        return valeurjeu, banque

    """
    Gestion du comportement en fonction de la main de la banque
    """
    def gestionComportementEnFonctionMainBanque(self, valeurBanque, mainBanque,montant, joueur, valeurJoueur, mainJoueur):
        if (valeurJoueur == 21 and len(mainJoueur) == 2) or (valeurBanque == 21 and len(mainBanque) == 2):
            blackjack = True
        else:
            blackjack = False

        if valeurBanque > 21 and valeurJoueur <= 21 and not blackjack:
            print("La banque a dépassé 21. Vous avez gagné !")
            self.solde -= 2 * montant
            joueur.argent += 2 * montant
        elif valeurJoueur > 21 and valeurBanque <= 21 and not blackjack:
            print("Vous avez dépassé 21. Vous avez perdu !")
            self.solde += 2 * montant
        elif (valeurBanque == 21 and len(mainBanque) == 2) and (valeurJoueur != 21 and len(mainJoueur) != 2):
            print("Blackjack pour la banque ! Vous avez perdu !")
            self.solde += 2 * montant
        elif (valeurBanque == 21 and len(mainBanque) == 2) and (valeurJoueur == 21 and len(mainJoueur) != 2):
            print("Égalité avec un Blackjack ! Vous récupérez votre mise.")
            joueur.argent += montant
        elif (valeurJoueur == 21 and len(mainJoueur) == 2) and (valeurBanque != 21 and len(mainBanque) != 2):
            print("Blackjack ! Vous avez gagné !")
            self.solde -= 2.5 * montant
            joueur.argent += 2.5 * montant
        else:
            if valeurBanque < valeurJoueur:
                print("Vous avez", valeurJoueur, "points et la banque a", valeurBanque, "points. Vous avez gagné !")
                self.solde -= 2 * montant
                joueur.argent += 2 * montant
            elif valeurBanque == valeurJoueur:
                print("Égalité ! Vous récupérez votre mise.")
                joueur.argent += montant
            else:
                print("Vous avez", valeurJoueur, "points et la banque a", valeurBanque, "points. Vous avez perdu !")
                self.solde += 2 * montant