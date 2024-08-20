# classes/medecin.py

from .personnel_medical import PersonelMedical

class Medecin(PersonelMedical):
    def __init__(self, nom, prenom, specialite, numero_licence, liste_patients=None):
        super().__init__(nom, prenom, specialite)
        self.numero_licence = numero_licence
        self.liste_patients = liste_patients or []

    def ajouter_patient(self, client):
        self.liste_patients.append(client)

    def afficher_info(self):
        super().afficher_info()
        print(f"Numéro de licence : {self.numero_licence}")
        print(f"Nombre de patients : {len(self.liste_patients)}")
