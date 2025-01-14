from flask import Blueprint, request, jsonify
from config import db, cursor

preferences_bp = Blueprint('preferences', __name__)

@preferences_bp.route('/preferences', methods=['POST'])

def add_preference():
    data = request.json
    utilisateur_id = data['utilisateur_id']
    activite_id = data['activite_id']

    try:
        # Vérifier si l'activité est déjà sélectionnée
        cursor.execute("SELECT * FROM Preferences WHERE utilisateur_id = %s AND activite_id = %s", (utilisateur_id, activite_id))
        existing_preference = cursor.fetchone()

        if existing_preference:
            return jsonify({"message": "Cette activité est déjà sélectionnée"}), 200

        # Ajouter la nouvelle préférence
        cursor.execute(
            "INSERT INTO Preferences (utilisateur_id, activite_id) VALUES (%s, %s)",
            (utilisateur_id, activite_id)
        )
        db.commit()
        return jsonify({"message": "Activité ajoutée aux préférences"}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400

@preferences_bp.route('/preferences/<int:utilisateur_id>', methods=['GET'])
def get_preferences(utilisateur_id):
    cursor.execute("""
        SELECT P.id, A.nom, A.description 
        FROM Preferences P 
        JOIN Activites A ON P.activite_id = A.id 
        WHERE P.utilisateur_id = %s
    """, (utilisateur_id,))
    preferences = cursor.fetchall()
    return jsonify(preferences)