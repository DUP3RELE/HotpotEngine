from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.restaurants import Restaurant

protected_bp = Blueprint('protected_bp', __name__, url_prefix='/api')


@protected_bp.route('/protected', methods=['GET'])
@jwt_required()
def get_protected():
    current_restaurant_id = get_jwt_identity()
    restaurant = Restaurant.query.get(current_restaurant_id)

    if not restaurant:
        return jsonify({"msg": "Użytkownik nie znaleziony"}), 404

    return jsonify({"restaurantname": restaurant.restaurantname}), 200
