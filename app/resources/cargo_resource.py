from flask import jsonify, Blueprint, request
from app.mapping.cargo_schema import CargoSchema
from app.models.cargo import Cargo
from app.services.cargo_service import CargoService
from app import db

cargo_bp = Blueprint('cargo', __name__)
cargo_schema = CargoSchema()
cargos_schema = CargoSchema(many=True)

@cargo_bp.route('/cargo', methods=['GET'])
def buscar_todos():
    cargos = CargoService.buscar_todos()
    return jsonify(cargos_schema.dump(cargos)), 200

@cargo_bp.route('/cargo/<string:nombre>', methods=['GET'])
def buscar_por_nombre(nombre):
    cargo = CargoService.buscar_por_nombre(nombre)
    if cargo is None:
        return jsonify({"error": "Cargo no encontrado"}), 404
    return jsonify(cargo_schema.dump(cargo)), 200

@cargo_bp.route('/cargo', methods=['POST'])
def crear():
    data = request.get_json()
    try:
        cargo = cargo_schema.load(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    db.session.add(cargo)
    db.session.commit()
    return jsonify(cargo_schema.dump(cargo)), 201

@cargo_bp.route('/cargo/<string:nombre>', methods=['DELETE'])
def borrar_por_nombre(nombre):
    cargo = CargoService.buscar_por_nombre(nombre)
    if not cargo:
        return jsonify({"error": "Cargo no encontrado"}), 404
    db.session.delete(cargo)
    db.session.commit()
    return jsonify({"mensaje": "Cargo borrado exitosamente"}), 200