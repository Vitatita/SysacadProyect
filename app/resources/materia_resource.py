from flask import jsonify, Blueprint, request
from app.mapping.materia_schema import MateriaSchema
from app.services.materia_service import MateriaService

materia_bp = Blueprint('materia', __name__)
materia_schema = MateriaSchema()

@materia_bp.route('/materias', methods=['GET'])
def get_materias():
    materias = MateriaService.get_all_materias()
    return jsonify([materia_schema.dump(m) for m in materias]), 200

@materia_bp.route('/materias', methods=['POST'])
def create_materia():
    data = request.get_json()
    materia = MateriaService.create_materia(**data)
    return jsonify(MateriaMapping.to_dict(materia)), 201

@materia_bp.route('/materias/<int:materia_id>', methods=['GET'])
def get_materia(materia_id):
    materia = MateriaService.get_materia(materia_id)
    if materia:
        return jsonify(MateriaMapping.to_dict(materia))
    return jsonify({'message': 'Materia not found'}), 404

@materia_bp.route('/materias/<int:materia_id>', methods=['PUT'])
def update_materia(materia_id):
    data = request.get_json()
    materia = MateriaService.update_materia(materia_id, **data)
    if materia:
        return jsonify(MateriaMapping.to_dict(materia))
    return jsonify({'message': 'Materia not found'}), 404

@materia_bp.route('/materias/<int:materia_id>', methods=['DELETE'])
def delete_materia(materia_id):
    deleted = MateriaService.delete_materia(materia_id)
    if deleted:
        return jsonify({'message': 'Materia deleted successfully'})
    return jsonify({'message': 'Materia not found'}), 404