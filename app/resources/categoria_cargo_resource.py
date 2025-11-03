from flask import jsonify, Blueprint, request
from app.mapping.categoria_cargo_schema import CategoriaCargoSchema
from app.models.categoria_cargo import CategoriaCargo
from app.services.categoria_cargo_service import CategoriaCargoService
from app import db

categoria_cargo_bp = Blueprint('categoria_cargo', __name__)
categoria_cargo_schema = CategoriaCargoSchema()
categorias_cargo_schema = CategoriaCargoSchema(many=True)

@categoria_cargo_bp.route('/categoria_cargo', methods=['GET'])
def buscar_todos():
    categorias = CategoriaCargoService.buscar_todos()
    return jsonify(categorias_cargo_schema.dump(categorias)), 200

@categoria_cargo_bp.route('/categoria_cargo/<int:id>', methods=['GET'])
def buscar_por_id(id):
    categoria = CategoriaCargoService.buscar_por_id(id)
    if categoria is None:
        return jsonify({"error": "Categoría no encontrada"}), 404
    return jsonify(categoria_cargo_schema.dump(categoria)), 200

@categoria_cargo_bp.route('/categoria_cargo', methods=['POST'])
def crear():
    data = request.get_json()
    try:
        nueva_categoria = categoria_cargo_schema.load(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify(categoria_cargo_schema.dump(nueva_categoria)), 201

@categoria_cargo_bp.route('/categoria_cargo/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    categoria = CategoriaCargoService.buscar_por_id(id)
    if not categoria:
        return jsonify({"error": "Categoría no encontrada"}), 404
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({"mensaje": "Categoría borrada exitosamente"}), 200