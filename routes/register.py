from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import db
from models.users import User

register_bp = Blueprint('register_bp', __name__, url_prefix='/api')

@register_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email is already in use'}), 409

    new_user = User(username=username, email=email)
    new_user.password_hash = generate_password_hash(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'uzytkownik zarejestrowany poprawnie'}), 201
