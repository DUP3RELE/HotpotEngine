from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models.restaurants import Restaurant
from flask_jwt_extended import create_access_token
from datetime import timedelta

login_bp = Blueprint('login_bp', __name__, url_prefix='/api')


@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Wpisz email i hasło'}), 400

    restaurant = Restaurant.query.filter_by(email=data.get('email')).first()

    if restaurant is None:
        return jsonify({'message': 'Nieprawidłowy adres E-mail'}), 401

    if not check_password_hash(restaurant.password_hash, password):
        return jsonify({'message': 'Niepoprawne hasło'}), 401

    if restaurant and check_password_hash(restaurant.password_hash, data.get('password')):
        additional_claims = {"restaurant_id": restaurant.id}
        access_token = create_access_token(identity=restaurant.id, additional_claims=additional_claims,
                                           expires_delta=timedelta(days=1))
        return jsonify(
            {'access_token': access_token, 'restaurant_id': restaurant.id, 'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401
