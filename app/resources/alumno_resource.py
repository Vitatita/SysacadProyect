from flask import Blueprint, request, jsonify
from app.services.alumno_service import AlumnoService

# 1. Aquí definimos "alumno_bp" para que deje de dar error "not defined"
alumno_bp = Blueprint('alumno_bp', __name__)

@alumno_bp.route('/scda/importar/alumnos', methods=['POST'])
def cargar_alumnos_scda():
    # 2. Ahora "request" y "jsonify" funcionarán porque los importamos arriba
    if 'file' not in request.files:
        return jsonify({"error": "No se envió el archivo"}), 400
    
    archivo = request.files['file']

    if archivo.filename.upper() != 'ALUMNOS.TXT':
        return jsonify({"error": "El archivo debe llamarse ALUMNOS.TXT"}), 400

    try:
        # Llamamos al servicio que creamos antes
        resultado = AlumnoService.importar_archivo_txt(archivo)
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({"error_critico": str(e)}), 500