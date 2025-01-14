import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Assurer que backend/ est bien chargé

from flask import Flask
from flask_cors import CORS
from routes.utilisateurs import utilisateurs_bp
from routes.objectifs import objectifs_bp
from routes.activites import activites_bp
from routes.exercices import exercices_bp
from routes.horaires import horaires_bp
from routes.preferences import preferences_bp

app = Flask(__name__)  # Création de l'application Flask
CORS(app)  # Autoriser les requêtes entre le frontend et le backend

# Enregistrer les routes
app.register_blueprint(utilisateurs_bp)
app.register_blueprint(objectifs_bp)
app.register_blueprint(activites_bp)
app.register_blueprint(exercices_bp)
app.register_blueprint(horaires_bp)
app.register_blueprint(preferences_bp)

if __name__ == '__main__':
    app.run(debug=True)  # Lancer le serveur Flask

