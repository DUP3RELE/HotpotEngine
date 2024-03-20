from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.users import User

protected_bp = Blueprint('protected_bp', __name__, url_prefix='/api')

@protected_bp.route('/protected', methods=['GET'])
@jwt_required()
def get_protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"msg": "Użytkownik nie znaleziony"}), 404

    return jsonify(username=user.username), 200
