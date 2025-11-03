from flask import jsonify, Blueprint, request
from app.mapping.departamento_schema import DepartamentoSchema
from app.models.departamento import Departamento
from app.services.departamento_service import DepartamentoService
from app import db

departamento_bp = Blueprint('departamento', __name__)
departamento_schema = DepartamentoSchema()
departamentos_schema = DepartamentoSchema(many=True)

@departamento_bp.route('/departamento', methods=['GET'])
def buscar_todos():
    departamentos = DepartamentoService.buscar_todos()
    return jsonify(departamentos_schema.dump(departamentos)), 200

@departamento_bp.route('/departamento/<int:id>', methods=['GET'])
def buscar_por_id(id):
    departamento = DepartamentoService.buscar_por_id(id)
    if departamento is None:
        return jsonify({"error": "Departamento no encontrado"}), 404
    return jsonify(departamento_schema.dump(departamento)), 200

@departamento_bp.route('/departamento', methods=['POST'])
def crear():
    data = request.get_json()
    try:
        nuevo_departamento = departamento_schema.load(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    db.session.add(nuevo_departamento)
    db.session.commit()
    return jsonify(departamento_schema.dump(nuevo_departamento)), 201

@departamento_bp.route('/departamento/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    departamento = DepartamentoService.buscar_por_id(id)
    if not departamento:
        return jsonify({"error": "Departamento no encontrado"}), 404
    db.session.delete(departamento)
    db.session.commit()
    return jsonify({"mensaje": "Departamento borrado exitosamente"}), 200