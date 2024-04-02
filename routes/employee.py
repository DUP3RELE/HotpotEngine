from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, employees

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/register_employee', methods=['POST'])
@jwt_required()
def register_employee():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    login = request.json.get('login', None)
    password = request.json.get('password', None)
    name = request.json.get('name', None)
    position = request.json.get('position', None)
    # Pobierz id restauracji z identyfikatora JWT
    restaurant_id = get_jwt_identity()

    if not login or not password or not name or not position:
        return jsonify({"msg": "Missing argument"}), 400
    
    # Sprawdź, czy login już istnieje
    if employees.query.filter_by(login=login).first():
        return jsonify({"msg": "Employee with this login already exists"}), 409

    new_employee = employees(login=login, password=password, name=name, position=position, restaurant_id=restaurant_id)
    db.session.add(new_employee)
    db.session.commit()

    return jsonify({"msg": "Employee registered", "employee_id": new_employee.id}), 201
