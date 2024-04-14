from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models import Employee
from flask_cors import CORS

employees_bp = Blueprint('employees_bp', __name__, url_prefix='/api')
CORS(employees_bp)

CORS(employees_bp, resources={r"/employees*": {"origins": "*"}})


@employees_bp.route('/employees', methods=['GET'])
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
