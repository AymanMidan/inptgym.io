from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from config import db, cursor

utilisateurs_bp = Blueprint('utilisateurs', __name__)

@utilisateurs_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['mot_de_passe'])

    try:
        cursor.execute(
            "INSERT INTO Utilisateurs (nom, prenom, email, mot_de_passe, genre) VALUES (%s, %s, %s, %s, %s)",
            (data['nom'], data['prenom'], data['email'], hashed_password, data['genre'])
        )
        db.commit()
        return jsonify({"message": "Inscription réussie"}), 201
    except Exception as e:
        db.rollback()  # Annule la transaction en cas d'erreur
        return jsonify({"error": str(e)}), 400

@utilisateurs_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    cursor.execute("SELECT id, nom, prenom, email, mot_de_passe FROM Utilisateurs WHERE email = %s", (data['email'],))
    user = cursor.fetchone()  # Avec `dictionary=True`, ceci retourne un dictionnaire

    if user:
        if check_password_hash(user["mot_de_passe"], data['mot_de_passe']):
            return jsonify({
                "message": "Connexion réussie",
                "user": {
                    "id": user["id"],
                    "nom": user["nom"],
                    "prenom": user["prenom"],
                    "email": user["email"]
                }
            }), 200
        else:
            return jsonify({"error": "Mot de passe incorrect"}), 401
    else:
        return jsonify({"error": "Email non trouvé"}), 404
