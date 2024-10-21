from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from models.restaurants import Restaurant
from models.employees import Employee

protected_bp = Blueprint('protected_bp', __name__, url_prefix='/api')


@protected_bp.route('/protected', methods=['GET'])
@jwt_required()
def get_protected():
    current_user_id = get_jwt_identity()
    user_type = get_jwt().get('userType')

    if user_type == 'restaurant':
        restaurant = Restaurant.query.get(current_user_id)
        if not restaurant:
            return jsonify({"msg": "Użytkownik nie znaleziony"}), 404
        return jsonify({"restaurantname": restaurant.restaurantname}), 200

    elif user_type == 'employee':
        employee = Employee.query.get(current_user_id)
        if not employee:
            return jsonify({"msg": "Użytkownik nie znaleziony"}), 404
        return jsonify({
            "employeename": employee.name,
            "employeeposition": employee.position
        }), 200

    return jsonify({"msg": "Niepoprawny typ użytkownika"}), 400