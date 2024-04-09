from flask import request, jsonify, Blueprint
from models import db, Employee
from flask_jwt_extended import jwt_required, get_jwt_identity

employee_bp = Blueprint('employee_bp', __name__, url_prefix='/api')

@employee_bp.route('/create_employee', methods=['POST'])
@jwt_required()
def create_employee():
    restaurant_id = get_jwt_identity()
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')
    name = data.get('name')
    position = data.get('position')

    if Employee.query.filter_by(login=login).first():
        return jsonify({'message': 'Pracownik o takim loginie już istnieje'}), 400

    new_employee = Employee(
        restaurant_id=restaurant_id,
        login=login,
        name=name,
        position=position
    )
    new_employee.set_password(password)

    db.session.add(new_employee)
    db.session.commit()

    return jsonify({'message': 'Pracownik został pomyślnie utworzony'}), 201
