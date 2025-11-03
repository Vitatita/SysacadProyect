from flask import jsonify, Blueprint, request
from app.mapping.orientacion_schema import OrientacionSchema
from app.services.orientacion_service import OrientacionService

orientacion_bp = Blueprint('orientacion', __name__)
orientacion_schema = OrientacionSchema()

@orientacion_bp.route('/orientaciones', methods=['POST'])
def create_orientacion():
    data = request.get_json()
    orientacion = OrientacionService.create_orientacion(**data)
    return jsonify(orientacion_schema.dump(orientacion)), 201

@orientacion_bp.route('/orientaciones/<int:orientacion_id>', methods=['GET'])
def get_orientacion(orientacion_id):
    orientacion = OrientacionService.get_orientacion(orientacion_id)
    if orientacion:
        return jsonify(OrientacionMapping.to_dict(orientacion))
    return jsonify({'message': 'Orientacion not found'}), 404

@orientacion_bp.route('/orientaciones/<int:orientacion_id>', methods=['PUT'])
def update_orientacion(orientacion_id):
    data = request.get_json()
    orientacion = OrientacionService.update_orientacion(orientacion_id, **data)
    if orientacion:
        return jsonify(OrientacionMapping.to_dict(orientacion))
    return jsonify({'message': 'Orientacion not found'}), 404

@orientacion_bp.route('/orientaciones/<int:orientacion_id>', methods=['DELETE'])
def delete_orientacion(orientacion_id):
    orientacion = OrientacionService.delete_orientacion(orientacion_id)
    if orientacion:
        return jsonify({'message': 'Orientacion deleted successfully'})
    return jsonify({'message': 'Orientacion not found'}), 404
