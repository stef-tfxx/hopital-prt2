# classes/client.py

class Client:
    def __init__(self, nom, prenom, date_naissance, adresse, numero_telephone):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.numero_telephone = numero_telephone
        self.liste_rdv = []

    def prendre_rdv(self, rdv):
        self.liste_rdv.append(rdv)
        print(f"Rendez-vous ajouté pour {self.nom} {self.prenom}.")

    def annuler_rdv(self, rdv):
        if rdv in self.liste_rdv:
            self.liste_rdv.remove(rdv)
            print(f"Rendez-vous annulé pour {self.nom} {self.prenom}.")
        else:
            print(f"Aucun rendez-vous correspondant trouvé pour {self.nom} {self.prenom}.")
