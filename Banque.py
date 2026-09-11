class Banque:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

    def GestionBanqueRéponse(self, banque, deck, valeurjeu):
        choix=False
        while choix==False:
            if valeurjeu<17:
                banque.append(deck.deck.pop())
                valeurjeu = deck.valeurMain(banque)
                print("Main de la banque :", banque, "Valeur :", valeurjeu)
            else:
                choix=True