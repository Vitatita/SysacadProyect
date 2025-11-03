from flask import Blueprint, jsonify, request
from app.mapping.especialidad_schema import EspecialidadSchema
from app.models.especialidad import Especialidad
from app.services.especialidad_service import EspecialidadService
from app import db

especialidad_bp = Blueprint('especialidad', __name__)
especialidad_schema = EspecialidadSchema()
especialidades_schema = EspecialidadSchema(many=True)

@especialidad_bp.route('/especialidad', methods=['GET'])
def buscar_todas():
    especialidades = EspecialidadService.buscar_todas()
    return jsonify(especialidades_schema.dump(especialidades)), 200

@especialidad_bp.route('/especialidad/<string:nombre>/<string:letra>', methods=['GET'])
def buscar_por_clave(nombre, letra):
    especialidad = EspecialidadService.buscar_por_clave(nombre, letra)
    if especialidad is None:
        return jsonify({"error": "Especialidad no encontrada"}), 404
    return jsonify(especialidad_schema.dump(especialidad)), 200

@especialidad_bp.route('/especialidad', methods=['POST'])
def crear():
    data = request.get_json()
    try:
        nueva_especialidad = especialidad_schema.load(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    db.session.add(nueva_especialidad)
    db.session.commit()
    return jsonify(especialidad_schema.dump(nueva_especialidad)), 201

@especialidad_bp.route('/especialidad/<string:nombre>/<string:letra>', methods=['DELETE'])
def borrar_por_clave(nombre, letra):
    especialidad = EspecialidadService.buscar_por_clave(nombre, letra)
    if not especialidad:
        return jsonify({"error": "Especialidad no encontrada"}), 404
    db.session.delete(especialidad)
    db.session.commit()
    return jsonify({"mensaje": "Especialidad borrada exitosamente"}), 200