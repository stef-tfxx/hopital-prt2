# classes/infirmier.py

from .personnel_medical import PersonelMedical

class Infirmier(PersonelMedical):
    def __init__(self, nom, prenom, specialite, numero_licence):
        super().__init__(nom, prenom, specialite)
        self.numero_licence = numero_licence

    def afficher_info(self):
        super().afficher_info()
        print(f"Numéro de licence : {self.numero_licence}")
