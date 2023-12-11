import os
from gestion_clients import GestionClients
from gestion_plats import GestionPlats
from gestion_commandes import GestionCommandes

class InterfaceUtilisateur:
    def __init__(self):
        self.gestion_clients = GestionClients()
        self.gestion_plats = GestionPlats()
        self.gestion_commandes = GestionCommandes()

    def menu_principal(self):
        while True:
            os.system('clear')

            print("\nMenu Principal:")
            print("1. Gérer les clients")
            print("2. Gérer les plats")
            print("3. Prendre une commande")
            print("4. Afficher les commandes")
            print("5. Exporter les commandes")
            print("6. Quitter")

            choix = input("Choisissez une option (1-6): ")

            if choix == '1':
                self.menu_gestion_clients()
            elif choix == '2':
                self.menu_gestion_plats()
            elif choix == '3':
                self.menu_prendre_commande()
            elif choix == '4':
                self.gestion_commandes.afficher_commandes()
            elif choix == '5':
                self.exporter_commandes()
            elif choix == '6':
                print("Au revoir!")
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

    def menu_gestion_clients(self):
        while True:

            print("\nMenu Gestion des Clients:")
            print("1. Afficher la liste des clients")
            print("2. Créer un nouveau client")
            print("3. Supprimer un client")
            print("4. Retour au menu principal")

            choix = input("Choisissez une option (1-4): ")

            if choix == '1':
                self.gestion_clients.afficher_clients()
            elif choix == '2':
                self.creer_nouveau_client()
            elif choix == '3':
                self.supprimer_client()
            elif choix == '4':
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")

    def menu_gestion_plats(self):
        while True:

            print("\nMenu Gestion des Plats:")
            print("1. Afficher la liste des plats")
            print("2. Créer un nouveau plat")
            print("3. Supprimer un plat")
            print("4. Retour au menu principal")

            choix = input("Choisissez une option (1-4): ")

            if choix == '1':
                self.gestion_plats.afficher_plats()
            elif choix == '2':
                self.creer_nouveau_plat()
            elif choix == '3':
                self.supprimer_plat()
            elif choix == '4':
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")


    def menu_prendre_commande(self):

        print("\nMenu Prendre une Commande:")

        id_client = input("Entrez l'ID du client: ")
        plats_commandes = input("Entrez les plats commandés (séparés par des virgules): ").split(',')

        self.gestion_commandes.prendre_commande(id_client, plats_commandes)
        print("Commande enregistrée avec succès.")

    def creer_nouveau_client(self):
        identifiant = input("Entrez l'identifiant du client: ")
        nom = input("Entrez le nom du client: ")
        prenom = input("Entrez le prénom du client: ")
        numero_telephone = input("Entrez le numéro de téléphone du client: ")

        self.gestion_clients.creer_client(identifiant, nom, prenom, numero_telephone)
        print("Nouveau client créé avec succès.")

    def supprimer_client(self):
        identifiant = input("Entrez l'identifiant du client à supprimer: ")
        self.gestion_clients.supprimer_client(identifiant)

    def creer_nouveau_plat(self):
        nom = input("Entrez le nom du plat: ")
        description = input("Entrez la description du plat: ")
        prix = input("Entrez le prix du plat: ")
        categorie = input("Entrez la catégorie du plat: ")

        self.gestion_plats.creer_plat(nom, description, prix, categorie)
        print("Nouveau plat créé avec succès.")

    def supprimer_plat(self):
        nom = input("Entrez le nom du plat à supprimer: ")
        self.gestion_plats.supprimer_plat(nom)

    def exporter_commandes(self):
        try:
            date_export = input("Entrez la date pour l'exportation (format YYYY-MM-DD): ")
            self.gestion_commandes.exporter_commandes(date_export)
            print(f"Exportation des commandes pour {date_export} réussie.")
        except Exception as e:
            print(f"Erreur lors de l'exportation des commandes : {str(e)}")
