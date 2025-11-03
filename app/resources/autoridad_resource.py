from flask import jsonify, Blueprint, request
from marshmallow import ValidationError
from app.mapping.autoridad_schema import AutoridadSchema
from app.services.autoridad_service import AutoridadService

autoridad_bp = Blueprint('autoridad', __name__)
autoridad_mapping = AutoridadSchema()

# Obtener todas las autoridades
@autoridad_bp.route('/autoridad', methods=['GET'])
def buscar_todas():
    autoridades = AutoridadService.buscar_todas()
    return autoridad_mapping.dump(autoridades, many=True), 200

# Obtener autoridad por ID
@autoridad_bp.route('/autoridad/<int:id>', methods=['GET'])
def buscar_por_id(id):
    autoridad = AutoridadService.buscar_por_id(id)
    if autoridad is None:
        return jsonify({"error": "Autoridad no encontrada"}), 404
    return autoridad_mapping.dump(autoridad), 200

# Crear nueva autoridad
@autoridad_bp.route('/autoridad', methods=['POST'])
def crear():
    try:
        # Validamos y deserializamos el JSON recibido
        autoridad_data = autoridad_mapping.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Creamos la autoridad en la DB
    autoridad = AutoridadService.crear(autoridad_data)

    # Devolvemos la autoridad creada en JSON
    return jsonify(autoridad_mapping.dump(autoridad)), 201

# Borrar autoridad por ID
@autoridad_bp.route('/autoridad/<int:id>', methods=['DELETE'])
def borrar_por_id(id):
    eliminado = AutoridadService.borrar_por_id(id)
    if not eliminado:
        return jsonify({"error": "Autoridad no encontrada"}), 404
    return jsonify({"mensaje": "Autoridad borrada exitosamente"}), 200

