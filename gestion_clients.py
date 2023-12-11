import json

class Client:
    def __init__(self, identifiant, nom, prenom, numero_telephone):
        self.identifiant = identifiant
        self.nom = nom
        self.prenom = prenom
        self.numero_telephone = numero_telephone

class GestionClients:
    def __init__(self, fichier_clients='clients.json'):
        self.fichier_clients = fichier_clients
        self.clients = self.charger_clients()

    def charger_clients(self):
        try:
            with open(self.fichier_clients, 'r') as file:
                data = json.load(file)
                return [Client(**client_data) for client_data in data]
        except FileNotFoundError:
            return []

    def creer_client(self, identifiant, nom, prenom, numero_telephone):
        if not self.client_existe(identifiant):
            nouveau_client = Client(identifiant, nom, prenom, numero_telephone)
            self.clients.append(nouveau_client)
            self.sauvegarder_clients()
        else:
            print(f"Le client avec l'ID {identifiant} existe déjà.")

    def supprimer_client(self, identifiant):
        client_a_supprimer = next((client for client in self.clients if client.identifiant == identifiant), None)
        if client_a_supprimer:
            self.clients.remove(client_a_supprimer)
            self.sauvegarder_clients()
            print(f"Client avec l'ID {identifiant} supprimé.")
        else:
            print(f"Aucun client trouvé avec l'ID {identifiant}.")

    def sauvegarder_clients(self):
        with open(self.fichier_clients, 'w') as file:
            data = [{'identifiant': client.identifiant, 'nom': client.nom, 'prenom': client.prenom, 'numero_telephone': client.numero_telephone} for client in self.clients]
            json.dump(data, file, indent=2)

    def afficher_clients(self):
        for client in self.clients:
            print(f"ID: {client.identifiant}, Nom: {client.nom}, Prénom: {client.prenom}, Téléphone: {client.numero_telephone}")

    def client_existe(self, identifiant):
        return any(client.identifiant == identifiant for client in self.clients)
