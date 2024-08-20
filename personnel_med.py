# classes/personnel_medical.py

class PersonelMedical:
    def __init__(self, nom, prenom, specialite):
        self.nom = nom
        self.prenom = prenom
        self.specialite = specialite

    def afficher_info(self):
        print(f"{self.nom} {self.prenom} - Spécialité : {self.specialite}")
