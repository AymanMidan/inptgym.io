from flask import Blueprint, request, jsonify
from config import db, cursor

activites_bp = Blueprint('activites', __name__)

@activites_bp.route('/activites', methods=['GET'])
def get_activites():
    cursor.execute("SELECT * FROM Activites")
    activites = cursor.fetchall()
    return jsonify(activites)

@activites_bp.route('/historique', methods=['POST'])
def add_historique():
    data = request.json
    cursor.execute("INSERT INTO Historique_Activites (utilisateur_id, activite_id, duree, calories_brules) VALUES (%s, %s, %s, %s)",
                   (data['utilisateur_id'], data['activite_id'], data['duree'], data['calories_brules']))
    db.commit()
    return jsonify({"message": "Activité ajoutée à l'historique"}), 201

@activites_bp.route('/historique/<int:utilisateur_id>', methods=['GET'])
def get_historique(utilisateur_id):
    cursor.execute("SELECT * FROM Historique_Activites WHERE utilisateur_id = %s", (utilisateur_id,))
    historique = cursor.fetchall()
    return jsonify(historique)
