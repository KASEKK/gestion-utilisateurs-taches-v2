# Parametres de connexion
scheme         = "postgresql+psycopg2"
username       = "postgres"
password       = "skmSKM01"
hostname       = "localhost"
port           = "5432"
database_name  = "gestion_utilisateurs"

# Construction de l'URL de connexion
URL_DB = f"{scheme}://{username}:{password}@{hostname}:{port}/{database_name}"