from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import db
from models.restaurants import Restaurant
import uuid

register_bp = Blueprint('register_bp', __name__, url_prefix='/api')

@register_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    restaurantname = data.get('restaurantname')
    email = data.get('email')
    password = data.get('password')

    if Restaurant.query.filter_by(email=email).first():
        return jsonify({'message': 'Email is already in use'}), 409

    def generate_restaurant_id():
        return uuid.uuid4().hex
    
    new_restaurant = Restaurant(restaurantname=restaurantname, email=email)
    new_restaurant.set_password(password)
    new_restaurant.restaurant_id = generate_restaurant_id()

    db.session.add(new_restaurant)
    db.session.commit()

    return jsonify({'message': 'Restaurant has been registered successfully'}), 201
