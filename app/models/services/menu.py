# app/menu.py

class Menu:
    def __init__(self, session):
        self.session = session

    def affichage(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Créer un utilisateur")
            print("2. Afficher tous les utilisateurs")
            print("3. Rechercher un utilisateur par email")
            print("4. Modifier un utilisateur")
            print("5. Supprimer un utilisateur")
            print("6. Créer une tâche pour un utilisateur")
            print("7. Afficher toutes les tâches")
            print("8. Afficher les tâches d’un utilisateur")
            print("9. Modifier une tâche")
            print("10. Supprimer une tâche")
            print("11. Quitter")

            choix = input("Votre choix : ")

            if choix == "1":
                print("→ Appel à la fonction : créer un utilisateur")
                # on appellera service_user.create_user(self.session)

            elif choix == "2":
                print("→ Appel à la fonction : afficher tous les utilisateurs")

            elif choix == "3":
                print("→ Appel à la fonction : rechercher un utilisateur")

            elif choix == "4":
                print("→ Appel à la fonction : modifier un utilisateur")

            elif choix == "5":
                print("→ Appel à la fonction : supprimer un utilisateur")

            elif choix == "6":
                print("→ Appel à la fonction : créer une tâche")

            elif choix == "7":
                print("→ Appel à la fonction : afficher toutes les tâches")

            elif choix == "8":
                print("→ Appel à la fonction : afficher les tâches d’un utilisateur")

            elif choix == "9":
                print("→ Appel à la fonction : modifier une tâche")

            elif choix == "10":
                print("→ Appel à la fonction : supprimer une tâche")

            elif choix == "11":
                print("👋 Au revoir !")
                break

            else:
                print("❌ Option invalide. Veuillez réessayer.")
