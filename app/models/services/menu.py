# app/menu.py

from app.models.services import task
from app.models.services import user
from app.models.services.user import (
    create_user,
    get_all_users,
    get_user_by_email,
    update_user,
    delete_user
)
from app.models.services.task import (
    create_task,
    get_all_tasks,
    get_tasks_by_user,
    update_task,
    delete_task
)



class Menu:
    def __init__(self, session):
        self.session = session

    def affichage(self):
        running = True
        while running:
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
                create_user(self.session)
            elif choix == "2":
                get_all_users(self.session)
            elif choix == "3":
                get_user_by_email(self.session)
            elif choix == "4":
                update_user(self.session)
            elif choix == "5":
                delete_user(self.session)
            elif choix == "6":
                create_task(self.session)
            elif choix == "7":
                get_all_tasks(self.session)
            elif choix == "8":
                get_tasks_by_user(self.session)
            elif choix == "9":
                update_task(self.session)
            elif choix == "10":
                delete_task(self.session)
            elif choix == "11":
                print("👋 Au revoir !")
                running = False  # <-- propre et clair
            else:
                print("❌ Option invalide. Veuillez réessayer.")

