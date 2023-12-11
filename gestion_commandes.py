# gestion_commandes.py
import json
import os

class GestionCommandes:
    def __init__(self, fichier_commandes='commandes.json'):
        self.fichier_commandes = fichier_commandes
        self.commandes = self.charger_commandes()

    def charger_commandes(self):
        try:
            with open(self.fichier_commandes, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def prendre_commande(self, id_client, plats_commandes):
        nouvelle_commande = {
            'id_client': id_client,
            'plats_commandes': plats_commandes
        }
        self.commandes.append(nouvelle_commande)
        self.sauvegarder_commandes()

    def supprimer_commande(self, id_client, plats_commandes):
        for commande in self.commandes:
            if commande['id_client'] == id_client and commande['plats_commandes'] == plats_commandes:
                self.commandes.remove(commande)
                self.sauvegarder_commandes()
                print(f"Commande pour le client ID {id_client} avec les plats {plats_commandes} supprimée.")
                return
        print(f"Aucune commande trouvée pour le client ID {id_client} avec les plats {plats_commandes}.")

    def sauvegarder_commandes(self):
        with open(self.fichier_commandes, 'w') as file:
            json.dump(self.commandes, file, indent=2)

    def afficher_commandes(self):
        for commande in self.commandes:
            print(f"ID Client: {commande['id_client']}, Plats Commandés: {commande['plats_commandes']}")

    def exporter_commandes(self, date_export):
        commandes_export = [commande for commande in self.commandes if commande.get('date_commande') == date_export]
        if commandes_export:
            nom_fichier_export = f"export_commandes_{date_export}.json"
            with open(nom_fichier_export, 'w') as file:
                json.dump(commandes_export, file, indent=2)
            print(f"Exportation des commandes pour {date_export} réussie. Fichier : {nom_fichier_export}")
        else:
            print(f"Aucune commande trouvée pour la date {date_export}.")
