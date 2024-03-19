from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models import db
from models.users import User

login_bp = Blueprint('login_bp', __name__, url_prefix='/api')

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data.get('email')).first()

    if user and check_password_hash(user.password_hash, data.get('password')):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
