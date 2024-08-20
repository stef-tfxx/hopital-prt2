# classes/liste_rdv.py

class ListeRDV:
    def __init__(self):
        self.rdv = []

    def ajouter_rdv(self, rdv):
        self.rdv.append(rdv)

    def afficher_rdv(self):
        for r in self.rdv:
            print(r)
