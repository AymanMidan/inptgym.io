from flask import Blueprint, request, jsonify
from config import db, cursor

horaires_bp = Blueprint('horaires', __name__)


@horaires_bp.route('/horaires', methods=['POST'])
def add_horaire():
    data = request.json
    utilisateur_id = data['utilisateur_id']
    horaires = data['horaires']  # Liste des horaires sélectionnés

    try:
        # Supprimer les anciens horaires de l'utilisateur
        cursor.execute("DELETE FROM Horaires WHERE utilisateur_id = %s", (utilisateur_id,))

        # Insérer les nouveaux horaires
        for horaire in horaires:
            jour, heure = horaire.split(" ")  # Séparer le jour et l'horaire
            cursor.execute(
                "INSERT INTO Horaires (utilisateur_id, jour, horaire) VALUES (%s, %s, %s)",
                (utilisateur_id, jour, heure)
            )

        db.commit()
        return jsonify({"message": "Horaires sauvegardés avec succès"}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400


@horaires_bp.route('/horaires/<int:utilisateur_id>', methods=['GET'])
def get_horaires(utilisateur_id):
    cursor.execute("SELECT * FROM Horaires WHERE utilisateur_id = %s", (utilisateur_id,))
    horaires = cursor.fetchall()
    return jsonify(horaires)