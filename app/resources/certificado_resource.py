from flask import jsonify, Blueprint, request, send_file
from app.services.certficado_service import CertificadoService

certificado_bp = Blueprint('certificado', __name__)

@certificado_bp.route('/certificado', methods=['POST'])
def generar_certificado():
    data = request.json
    alumno = data.get('alumno')
    especialidad = data.get('especialidad')
    facultad = data.get('facultad')
    universidad = data.get('universidad')

    if not all([alumno, especialidad, facultad, universidad]):
        return jsonify({"error": "Faltan datos"}), 400

    pdf_path = CertificadoService.generar_certificado(
        alumno, especialidad, facultad, universidad
    )
    # Descargar directamente
    return send_file(pdf_path, as_attachment=True)