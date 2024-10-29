from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models.restaurants import Restaurant
from models.employees import Employee
from flask_jwt_extended import create_access_token
from datetime import timedelta


login_bp = Blueprint('login_bp', __name__, url_prefix='/api')


@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    identifier = data.get('identifier')
    password = data.get('password')

    if not identifier or not password:
        return jsonify({'message': 'Wpisz email/login i hasło'}), 400

    restaurant = Restaurant.query.filter_by(email=identifier).first()
    if restaurant and check_password_hash(restaurant.password_hash, password):
        additional_claims = {"userType": "restaurant", "restaurant_id": restaurant.id}
        access_token = create_access_token(identity=restaurant.id, additional_claims=additional_claims,
                                           expires_delta=timedelta(days=1))
        return jsonify(
            {
                'access_token': access_token,
                'restaurant_id': restaurant.id,
                'userType': 'restaurant',
                'message': 'Login successful'
            }), 200

    employee = Employee.query.filter_by(login=identifier).first()
    if employee and check_password_hash(employee.password_hash, password):
        additional_claims = {"userType": "employee", "employee_id": employee.employee_id}
        access_token = create_access_token(identity=employee.employee_id, additional_claims=additional_claims,
                                           expires_delta=timedelta(days=1))
        return jsonify(
            {
                'access_token': access_token,
                'employee_id': employee.employee_id,
                'restaurant_id': employee.restaurant_id,
                'userType': 'employee',
                'message': 'Login successful'
            }), 200

    return jsonify({'message': 'Niepoprawny login lub hasło'}), 401
