import Banque
import Joueur
import Carte

class Blackjack:
    def __init__(self):
        self.joueur = Joueur.Joueur("Otmane", 1000)
        self.banque = Banque.Banque("Banque", 10000)
        self.carte = Carte.Carte()
        
    def main(self):
        print("Bienvenue dans le jeu de Blackjack !")
        self.carte.GenerationDeck()    
        self.carte.melange()
        mainCarte = self.carte.distributionCarte(self.carte.deck)
        mainBanque = self.carte.distributionCarte(self.carte.deck)
        print("Votre main :", mainCarte)
        print("Main de la banque :", mainBanque)

        self.joueur.GestionJoueuréponse(mainCarte,self.carte.deck)
        self.banque.GestionBanqueRéponse(mainBanque,self.carte.deck)


Blackjack().main()