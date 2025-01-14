from flask import Blueprint, request, jsonify
from config import db, cursor

exercices_bp = Blueprint('exercices', __name__)

@exercices_bp.route('/exercices', methods=['GET'])
def get_exercices():
    cursor.execute("SELECT * FROM Exercices")
    exercices = cursor.fetchall()
    return jsonify(exercices)
