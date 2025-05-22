# app/models/services/user.py
from app.models.db.task import Task
from app.models.db.user import User

def create_task(session):
    print("\n--- Création d’une nouvelle tâche ---")
    description = input("Description de la tâche : ")
    user_id = input("ID de l’utilisateur à qui attribuer la tâche : ")

    user = session.query(User).get(user_id)
    if user:
        task = Task(description=description, user_id=user.id)
        session.add(task)
        session.commit()
        print("✅ Tâche créée avec succès.")
    else:
        print("❌ Utilisateur non trouvé.")

def get_all_tasks(session):
    print("\n--- Liste de toutes les tâches ---")
    tasks = session.query(Task).all()
    if tasks:
        for task in tasks:
            print(f"[{task.id}] {task.description} - utilisateur ID : {task.user_id}")
    else:
        print("❌ Aucune tâche trouvée.")

def get_tasks_by_user(session):
    print("\n--- Tâches d’un utilisateur ---")
    user_id = input("ID de l’utilisateur : ")
    tasks = session.query(Task).filter_by(user_id=user_id).all()
    if tasks:
        for task in tasks:
            print(f"[{task.id}] {task.description}")
    else:
        print("❌ Aucune tâche trouvée pour cet utilisateur.")

def update_task(session):
    print("\n--- Modification d’une tâche ---")
    task_id = input("ID de la tâche à modifier : ")
    task = session.query(Task).get(task_id)

    if task:
        new_description = input(f"Nouvelle description (actuelle : {task.description}) : ")
        if new_description:
            task.description = new_description
            session.commit()
            print("✅ Tâche modifiée avec succès.")
        else:
            print("❌ Description vide. Aucune modification effectuée.")
    else:
        print("❌ Tâche non trouvée.")

def delete_task(session):
    print("\n--- Suppression d’une tâche ---")
    task_id = input("ID de la tâche à supprimer : ")
    task = session.query(Task).get(task_id)

    if task:
        confirmation = input(f"⚠️ Supprimer la tâche '{task.description}' ? (y/n) : ")
        if confirmation.lower() == "y":
            session.delete(task)
            session.commit()
            print("✅ Tâche supprimée.")
        else:
            print("❌ Suppression annulée.")
    else:
        print("❌ Tâche non trouvée.")




