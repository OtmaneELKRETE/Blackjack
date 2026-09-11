class Banque:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

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

    def gestionComportementEnFonctionMainBanque(self, valeurBanque, mainBanque):
        if valeurBanque > 21:
            print("La banque a dépassé 21. Vous avez gagné !")
        elif valeurBanque == 21 and len(mainBanque) == 2:
            print("Blackjack pour la banque ! Vous avez perdu !")
        else:
            print("La banque a", valeurBanque, "points.")