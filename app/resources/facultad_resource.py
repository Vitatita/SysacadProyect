from flask import jsonify, Blueprint, request
from marshmallow import ValidationError
from app.mapping.facultad_schema import FacultadSchema
from app.services.facultad_service import FacultadService

facultad_bp = Blueprint('facultad', __name__)
facultad_mapping = FacultadSchema()

@facultad_bp.route('/facultad', methods=['GET'])
def buscar_todas():
    facultades = FacultadService.buscar_todas()
    return facultad_mapping.dump(facultades, many=True), 200

@facultad_bp.route('/facultad/<int:id>', methods=['GET'])
def buscar_por_id(id):
    facultad = FacultadService.buscar_por_id(id)
    if facultad is None:
        return jsonify({"error": "Facultad no encontrada"}), 404
    return facultad_mapping.dump(facultad), 200

@facultad_bp.route('/facultad', methods=['POST'])
def crear():
    try:
        facultad = facultad_mapping.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400
    FacultadService.crear(facultad)
    return jsonify({"mensaje": "Facultad creada exitosamente"}), 201

@facultad_bp.route('/facultad/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    eliminado = FacultadService.borrar_por_id(id)
    if not eliminado:
        return jsonify({"error": "Facultad no encontrada"}), 404
    return jsonify({"mensaje": "Facultad borrada exitosamente"}), 200
