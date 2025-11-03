from flask import jsonify, Blueprint, request
from app.mapping.tipo_dedicacion_schema import TipoDedicacionSchema
from app.services.tipo_dedicacion_service import TipoDedicacionService

tipo_dedicacion_bp = Blueprint('tipo_dedicacion', __name__)
tipo_dedicacion_schema = TipoDedicacionSchema()


@tipo_dedicacion_bp.route('/tipo_dedicacion', methods=['POST'])
def create_tipo_dedicacion():
    data = request.get_json()
    tipo_dedicacion = TipoDedicacionService.create_tipo_dedicacion(**data)
    return jsonify(tipo_dedicacion_schema.dump(tipo_dedicacion)), 201

@tipo_dedicacion_bp.route('/tipo_dedicacion/<int:tipo_dedicacion_id>', methods=['GET'])
def get_tipo_dedicacion(tipo_dedicacion_id):
    tipo_dedicacion = TipoDedicacionService.get_tipo_dedicacion(tipo_dedicacion_id)
    if tipo_dedicacion:
        return jsonify(TipoDedicacionMapping.to_dict(tipo_dedicacion))
    return jsonify({'message': 'Tipo de dedicacion not found'}), 404

@tipo_dedicacion_bp.route('/tipo_dedicacion/<int:tipo_dedicacion_id>', methods=['PUT'])
def update_tipo_dedicacion(tipo_dedicacion_id):
    data = request.get_json()
    tipo_dedicacion = TipoDedicacionService.update_tipo_dedicacion(tipo_dedicacion_id, **data)
    if tipo_dedicacion:
        return jsonify(TipoDedicacionMapping.to_dict(tipo_dedicacion))
    return jsonify({'message': 'Tipo de dedicacion not found'}), 404

@tipo_dedicacion_bp.route('/tipo_dedicacion/<int:tipo_dedicacion_id>', methods=['DELETE'])
def delete_tipo_dedicacion(tipo_dedicacion_id):
    tipo_dedicacion = TipoDedicacionService.delete_tipo_dedicacion(tipo_dedicacion_id)
    if tipo_dedicacion:
        return jsonify({'message': 'Tipo de dedicacion deleted successfully'})
    return jsonify({'message': 'Tipo de dedicacion not found'}), 404
