# app/models/user.py
from app.models.db.user import User

def create_user(session):
    print("\n--- Création d’un nouvel utilisateur ---")
    username = input("Nom d’utilisateur : ")
    email = input("Email : ")
    password = input("Mot de passe : ")

    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()
    print("✅ Utilisateur créé avec succès.")

def get_all_users(session):
    print("\n--- Liste des utilisateurs ---")
    users = session.query(User).all()
    if users:
        for user in users:
            print(f"[{user.id}] {user.username} - {user.email} - Actif : {user.is_active}")
    else:
        print("❌ Aucun utilisateur trouvé.")

def get_user_by_email(session):
    print("\n--- Recherche d’un utilisateur par email ---")
    email = input("Email à rechercher : ")
    user = session.query(User).filter_by(email=email).first()
    if user:
        print(f"✅ Utilisateur trouvé : {user.username} (ID : {user.id})")
    else:
        print("❌ Aucun utilisateur trouvé avec cet email.")

def update_user(session):
    print("\n--- Modification d’un utilisateur ---")
    user_id = input("ID de l’utilisateur à modifier : ")
    user = session.query(User).get(user_id)

    if user:
        print(f"Utilisateur actuel : {user.username} - {user.email}")
        new_username = input("Nouveau nom (laisser vide pour ne pas changer) : ")
        new_email = input("Nouvel email (laisser vide pour ne pas changer) : ")
        new_password = input("Nouveau mot de passe (laisser vide pour ne pas changer) : ")

        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
        if new_password:
            user.password = new_password

        session.commit()
        print("✅ Utilisateur mis à jour avec succès.")
    else:
        print("❌ Utilisateur non trouvé.")


def delete_user(session):
    print("\n--- Suppression d’un utilisateur ---")
    user_id = input("ID de l’utilisateur à supprimer : ")
    user = session.query(User).get(user_id)

    if user:
        confirmation = input(f"⚠️ Confirmer suppression de {user.username} ? (y/n) : ")
        if confirmation.lower() == "y":
            session.delete(user)
            session.commit()
            print("✅ Utilisateur supprimé.")
        else:
            print("❌ Suppression annulée.")
    else:
        print("❌ Utilisateur non trouvé.")