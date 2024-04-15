from flask import request, jsonify, Blueprint
from models import db
from models.employees import Employee
from flask_jwt_extended import jwt_required

employee_bp = Blueprint('employee_bp', __name__, url_prefix='/api')


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
