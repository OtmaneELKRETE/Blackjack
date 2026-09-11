import Banque
import Joueur
import Carte

class Blackjack:
    def __init__(self):
        self.joueur = Joueur.Joueur("Otmane", 1000)
        self.banque = Banque.Banque("Banque", 10000)
        self.carte = Carte.Carte()
        
    def main(self):
        print("Bienvenue dans le jeu de Blackjack " + self.joueur.nom + " ! vous avez " + str(self.joueur.argent) + "€")
        self.carte.GenerationDeck()    
        self.carte.melange()
        mainjoueur = self.carte.distributionCarte(self.carte.deck)
        mainBanque = self.carte.distributionCarte(self.carte.deck)
        valeurJeu = self.carte.valeurMain(mainjoueur)
        valeurBanque = self.carte.valeurMain(mainBanque)
        print("Votre main :", mainjoueur, "Valeur :", valeurJeu)
        print("Main de la banque :", mainBanque, "Valeur :", valeurBanque)

        valeurJeu,mainjoueur = self.joueur.GestionJoueuréponse(mainjoueur, self.carte, valeurJeu)

        if self.joueur.gestionComportementEnFonctionMainJoueur(valeurJeu, mainjoueur):
            valeurBanque,mainBanque = self.banque.GestionBanqueRéponse(mainBanque, self.carte, valeurBanque)
            self.banque.gestionComportementEnFonctionMainBanque(valeurBanque, mainBanque)

Blackjack().main()