import json

class GestionPlats:
    def __init__(self, fichier_plats='plats.json'):
        self.fichier_plats = fichier_plats
        self.plats = self.charger_plats()

    def charger_plats(self):
        try:
            with open(self.fichier_plats, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def creer_plat(self, nom, description, prix, categorie):
        nouveau_plat = {
            'nom': nom,
            'description': description,
            'prix': prix,
            'categorie': categorie
        }
        self.plats.append(nouveau_plat)
        self.sauvegarder_plats()

    def supprimer_plat(self, nom):
        plat_trouve = next((plat for plat in self.plats if plat['nom'] == nom), None)
        if plat_trouve:
            self.plats.remove(plat_trouve)
            self.sauvegarder_plats()
            print(f"Plat avec le nom '{nom}' supprimé.")
        else:
            print(f"Aucun plat trouvé avec le nom '{nom}'.")

    def sauvegarder_plats(self):
        with open(self.fichier_plats, 'w') as file:
            json.dump(self.plats, file, indent=2)

    def afficher_plats(self):
        for plat in self.plats:
            print(f"Nom: {plat['nom']}, Description: {plat['description']}, Prix: {plat['prix']}, Catégorie: {plat['categorie']}")
