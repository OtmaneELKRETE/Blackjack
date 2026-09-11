class Banque:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

    def GestionBanqueRéponse(self, banque, deck):
        choix=False
        while choix==False:
            if len(banque)<17:
                banque.append(deck.deck.pop())
                valeur = deck.valeurMain(banque)
                print("Main de la banque :", banque, "Valeur :", valeur)
            else:
                choix=True