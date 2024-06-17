from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.employees import Employee

employee_name_bp = Blueprint('employee_name_bp', __name__, url_prefix="/api")


@employee_name_bp.route('/employee_name', methods=['GET'])
@jwt_required()
def get_employee_name():
    current_employee_id = get_jwt_identity()
    employee = Employee.query.get(current_employee_id)

    if not employee:
        return jsonify({"msg": "Użytkownik nie znaleziony"}), 404

    return jsonify({"employeename": employee.name, "employeeposition": employee.position}), 200
