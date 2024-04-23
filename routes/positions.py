from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.position import Position, db

position_bp = Blueprint('position_bp', __name__, url_prefix='/api')


@position_bp.route('/positions', methods=['GET'])
@jwt_required()
def get_positions():
    restaurant_id = request.args.get('restaurant_id')
    if not restaurant_id:
        return jsonify({"error": "Restaurant ID is required"}), 400

    positions = Position.query.filter_by(restaurant_id=restaurant_id).all()
    return jsonify([{
        "id": pos.id,
        "restaurant_id": pos.restaurant_id,
        "position": pos.position,
        "access": pos.access
    } for pos in positions])


@position_bp.route('/positions', methods=['POST'])
@jwt_required()
def create_position():
    data = request.json
    position = Position(
        restaurant_id=data['restaurant_id'],
        position=data['position'],
        access=data.get('access', '')
    )
    db.session.add(position)
    db.session.commit()
    return jsonify({"message": "Position created", "position": position.position}), 201


@position_bp.route('/positions/<int:position_id>', methods=['PUT'])
@jwt_required()
def update_position(position_id):
    data = request.json
    position = Position.query.get(position_id)
    if not position:
        return jsonify({"error": "Position not found"}), 404

    position.position = data.get('position', position.position)
    position.access = data.get('access', position.access)
    db.session.commit()

    return jsonify({"message": "Position updated", "position": position.position}), 200


@position_bp.route('/positions/<int:position_id>', methods=['DELETE'])
@jwt_required()
def delete_position(position_id):
    position = Position.query.get(position_id)
    if not position:
        return jsonify({"error": "Position not found"}), 404

    db.session.delete(position)
    db.session.commit()

    return jsonify({"message": "Position deleted"}), 200
