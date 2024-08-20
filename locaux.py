# classes/liste_locaux.py

class ListeLocaux:
    def __init__(self):
        self.locaux = []

    def ajouter_local(self, local):
        self.locaux.append(local)

    def afficher_locaux(self):
        for l in self.locaux:
            print(l)
