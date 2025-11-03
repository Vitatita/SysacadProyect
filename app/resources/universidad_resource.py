from flask import jsonify, Blueprint, request
from app.mapping.universidad_schema import UniversidadSchema
from app.services.universidad_service import UniversidadService
from markupsafe import escape

# from app.validators import validate_with (luego de hacer validators)
#corregir services

universidad_bp = Blueprint('universidad', __name__)
universidad_mapping = UniversidadSchema()

@universidad_bp.route('/universidad', methods=['GET'])
def buscar_todos():
    universidades = UniversidadService.buscar_todos()
    return universidad_mapping.dump(universidades, many=True), 200

@universidad_bp.route('/universidad/<hashid:id>', methods=['GET'])
def buscar_por_id(id):
    universidad = UniversidadService.buscar_universidad(id)
    return universidad_mapping.dump(universidad), 200

@universidad_bp.route('/universidad', methods=['POST'])
def crear():
    universidad = universidad_mapping.load(request.get_json())
    UniversidadService.crear(universidad)
    return jsonify({"mensaje": "Universidad creada exitosamente"}), 201 #201 significa creado exitosamente

@universidad_bp.route('/universidad/<hashid:id>', methods=['DELETE'])
def borrar_por_id(id):
    universidad = UniversidadService.borrar_por_id(id)
    return jsonify("Universidad borrada exitosamente"), 200 #200 significa que se borro exitosament

@universidad_bp.route('/universidad/<hashid:id>', methods=['PUT'])
#@validate_with(UniversidadMapping) #validar acciones con marshmallow 
def actualizar(id):
    universidad = universidad_mapping.load(request.get_json()) #cada vez que se llama al load sanitiza
    UniversidadService.actualizar_universidad(universidad, id)
    return jsonify("Universidad actualizada exitosamente"), 200

def sanitizar_universidad_entrada(request):
    universidad = universidad_mapping.load(request.get_json())
    universidad.nombre = escape(universidad.nombre)
    universidad.sigla = escape(universidad.sigla)
    universidad.tipo = escape(universidad.tipo) 
    return universidad