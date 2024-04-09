from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models import db
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
        return jsonify({'message': 'Email and password are required'}), 400
    
    restaurant = Restaurant.query.filter_by(email=data.get('email')).first()

    if restaurant and check_password_hash(restaurant.password_hash, data.get('password')):
        access_token = create_access_token(identity=restaurant.id, expires_delta=timedelta(days=1))
        return jsonify({'access_token': access_token, 'restaurant_id': restaurant.id, 'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401
