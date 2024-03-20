from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models import db
from models.users import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

login_bp = Blueprint('login_bp', __name__, url_prefix='/api')

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data.get('email')).first()

    if user and check_password_hash(user.password_hash, data.get('password')):
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=1))
        return jsonify({'access_token': access_token, 'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
