
class Joueur:
    def __init__(self, nom,argent):
        self.nom = nom
        self.argent = argent

    def GestionJoueuréponse(self, main, deck):
        choix=False
        while choix==False:
            reponse = input("Voulez-vous tirer une carte ? (oui/non) : ")
            if reponse == "oui":
                main.append(deck.pop())
                print("Votre main :", main)
            elif reponse == "non":
                choix=True