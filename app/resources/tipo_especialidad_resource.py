from flask import jsonify, Blueprint, request
from app.mapping.tipo_especialidad_schema import TipoEspecialidadSchema
from app.services.tipo_especialidad_service import TipoEspecialidadService

tipo_especialidad_bp = Blueprint('tipo_especialidad', __name__)
tipo_especialidad_schema = TipoEspecialidadSchema()


@tipo_especialidad_bp.route('/tipo_especialidad', methods=['POST'])
def create_tipo_especialidad():
    data = request.get_json()
    tipo_especialidad = TipoEspecialidadService.create_tipo_especialidad(**data)
    return jsonify(tipo_especialidad_schema.dump(tipo_especialidad)), 201

@tipo_especialidad_bp.route('/tipo_especialidad/<int:tipo_especialidad_id>', methods=['GET'])
def get_tipo_especialidad(tipo_especialidad_id):
    tipo_especialidad = TipoEspecialidadService.get_tipo_especialidad(tipo_especialidad_id)
    if tipo_especialidad:
        return jsonify(tipo_especialidad_schema.dump(tipo_especialidad))
    return jsonify({'message': 'Tipo de especialidad not found'}), 404

@tipo_especialidad_bp.route('/tipo_especialidad/<int:tipo_especialidad_id>', methods=['PUT'])
def update_tipo_especialidad(tipo_especialidad_id):
    data = request.get_json()
    tipo_especialidad = TipoEspecialidadService.update_tipo_especialidad(tipo_especialidad_id, **data)
    if tipo_especialidad:
        return jsonify(tipo_especialidad_schema.dump(tipo_especialidad))
    return jsonify({'message': 'Tipo de especialidad not found'}), 404

@tipo_especialidad_bp.route('/tipo_especialidad/<int:tipo_especialidad_id>', methods=['DELETE'])
def delete_tipo_especialidad(tipo_especialidad_id):
    tipo_especialidad = TipoEspecialidadService.delete_tipo_especialidad(tipo_especialidad_id)
    if tipo_especialidad:
        return jsonify({'message': 'Tipo de especialidad deleted successfully'})
    return jsonify({'message': 'Tipo de especialidad not found'}), 404
