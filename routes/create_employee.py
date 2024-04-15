from flask import request, jsonify, Blueprint
from models import db
from models.employees import Employee
from flask_jwt_extended import jwt_required

employee_bp = Blueprint('employee_bp', __name__, url_prefix='/api')

@employee_bp.route('/create_employee', methods=['POST'])
@jwt_required()
def create_employee():
    data = request.get_json()
    restaurant_id = data.get('restaurant_id')
    login = data.get('login')
    password = data.get('password')
    name = data.get('name')
    position = data.get('position')

    if not restaurant_id:
        return jsonify({'message': 'Brak restaurant_id'}), 400

    existing_employee = Employee.query.filter_by(login=login).first()
    if existing_employee:
        return jsonify({'message': 'Pracownik o takim loginie już istnieje'}), 400

    new_employee = Employee(
        restaurant_id=restaurant_id,
        login=login,
        name=name,
        position=position
    )
    new_employee.password = password

    db.session.add(new_employee)
    db.session.commit()

    return jsonify({'message': 'Pracownik został pomyślnie utworzony'}), 201

@employee_bp.route('/get_employees', methods=['GET'])
@jwt_required()
def get_employees():
    restaurant_id = request.args.get('restaurant_id')
    if not restaurant_id:
        return jsonify({'message': 'Brak ID restauracji w żądaniu'}), 400

    employees = Employee.query.filter_by(restaurant_id=restaurant_id).all()
    employees_list = [
        {"id": emp.employee_id, "name": emp.name, "position": emp.position}
        for emp in employees
    ]

    return jsonify(employees_list), 200
