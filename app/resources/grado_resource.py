from flask import jsonify, Blueprint, request
from app.services.grado_service import GradoService
from app.mapping.grado_schema import GradoSchema 

grado_bp = Blueprint('grado', __name__)
grado_schema = GradoSchema()  # instanciamos el schema


@grado_bp.route('/grados', methods=['GET'])
def get_grados():
    grados = GradoService.buscar_todas()
    return grado_schema.dump(grados, many=True), 200  # usamos dump del schema

@grado_bp.route('/grados/<int:id>', methods=['GET'])
def get_grado(id):
    grado = GradoService.buscar_por_id(id)
    if not grado:
        return jsonify({'error': 'Grado no encontrado'}), 404
    return jsonify(GradoMapping.detalle(grado)), 200

@grado_bp.route('/grados', methods=['POST'])
def create_grado():
    data = request.json
    grado = GradoService.crear(data)
    return jsonify(GradoMapping.detalle(grado)), 201

@grado_bp.route('/grados/<int:id>', methods=['DELETE'])
def delete_grado(id):
    if GradoService.borrar_por_id(id):
        return jsonify({'message': 'Grado eliminado'}), 200
    return jsonify({'error': 'Grado no encontrado'}), 404