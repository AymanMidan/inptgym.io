from flask import Blueprint, request, jsonify
from config import db, cursor

objectifs_bp = Blueprint('objectifs', __name__)

@objectifs_bp.route('/objectifs', methods=['POST'])
def add_objectif():
    data = request.json
    utilisateur_id = data['utilisateur_id']
    nombre_seances = data['nombre_seances']  # Récupérer le nombre de séances
    calories_a_bruler = data['calories_a_bruler']  # Récupérer les calories à brûler
    objectif_sante = data['objectif_sante']
    notes = data['notes']

    try:
        # Insérer tous les champs dans la base de données
        cursor.execute(
            "INSERT INTO Objectifs (utilisateur_id, nombre_seances, calories_a_bruler, objectif_sante, notes) VALUES (%s, %s, %s, %s, %s)",
            (utilisateur_id, nombre_seances, calories_a_bruler, objectif_sante, notes)
        )
        db.commit()
        return jsonify({"message": "Objectif enregistré avec succès"}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400

@objectifs_bp.route('/objectifs/<int:utilisateur_id>', methods=['GET'])
def get_objectifs(utilisateur_id):
    cursor.execute("SELECT * FROM Objectifs WHERE utilisateur_id = %s", (utilisateur_id,))
    objectifs = cursor.fetchall()
    return jsonify(objectifs)
