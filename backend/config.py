import mysql.connector

# Configuration de la connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change si nécessaire
    password="1a2b",  # Mets ton mot de passe MySQL si nécessaire
    database="InptGym"
)

# Curseur permettant d'exécuter les requêtes SQL
cursor = db.cursor(dictionary=True)
