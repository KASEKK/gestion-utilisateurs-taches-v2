# Projet Console - Gestion d'utilisateurs et de tâches

Ce projet est une application **console** développée en **Python** avec **SQLAlchemy** et **PostgreSQL**, permettant de gérer des utilisateurs et leurs tâches.

---

## Objectifs pédagogiques

- Apprendre à utiliser un **ORM (SQLAlchemy)** pour manipuler une base de données relationnelle sans écrire de requêtes SQL manuelles.
- Comprendre les notions de :
  - Création d’un modèle (classe ORM)
  - Connexion à une base PostgreSQL
  - Création automatique des tables
  - Fonctions CRUD (Créer, Lire, Modifier, Supprimer)
  - Structure modulaire d’un projet Python
- Développer une **interface console interactive** avec un menu utilisateur.

---

## Stack technique

| Outil          | Rôle                               |
|----------------|------------------------------------|
| Python 3.x     | Langage principal                  |
| SQLAlchemy     | ORM pour base de données relationnelle |
| PostgreSQL     | Système de base de données utilisé |
| pgAdmin        | Interface graphique pour PostgreSQL |
| Anaconda       | Environnement virtuel              |

---

## Structure du projet

```

projet/
├── app/
│   ├── config.py              ← Connexion à PostgreSQL
│   ├── main.py                ← Point d’entrée de l’application
│   ├── models/
│   │   └── db/
│   │       ├── base.py        ← ORM Base
│   │       ├── user.py        ← Modèle User
│   │       ├── task.py        ← Modèle Task
│   │       └── **init**.py
│   └── services/
│       ├── user.py            ← Fonctions CRUD utilisateurs
│       ├── task.py            ← Fonctions CRUD tâches
│       └── menu.py            ← Interface console
├── requirements.txt           ← Dépendances
└── README.md                  ← Ce fichier 🙂

````

---

## Lancer le projet

1. Cloner le repo :
   ```bash
   git clone https://github.com/ton_pseudo/nom_du_repo.git
   cd nom_du_repo
````

2. Activer ton environnement Anaconda :

   ```bash
   conda activate mon_env
   ```

3. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Créer ta base dans pgAdmin (ex: `gestion_utilisateurs`)
   ⚠ N’oublie pas de modifier `app/config.py` avec tes infos de connexion.

5. Lancer l'application :

   ```bash
   python -m app.main
   ```

---

## Fonctionnalités disponibles

* Utilisateurs :

  * Créer un utilisateur
  * Afficher tous les utilisateurs
  * Rechercher un utilisateur par email
  * Modifier un utilisateur
  * Supprimer un utilisateur

* Tâches :

  * Créer une tâche
  * Afficher toutes les tâches
  * Afficher les tâches d’un utilisateur
  * Modifier une tâche
  * Supprimer une tâche

---

## Améliorations possibles

* Ajout d’une interface web (ex: Flask)
* Export CSV des utilisateurs ou des tâches
* Authentification utilisateur
* Tests unitaires avec `pytest`
* Pagination ou recherche avancée

---

##  Auteur·rice

Projet réalisé par Sabrina Kosecki (KASEKK) dans un cadre pédagogique (exercice de formation full stack dev python).

```
