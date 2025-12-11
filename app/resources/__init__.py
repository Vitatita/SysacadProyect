from .home import home_bp
from .universidad_resource import universidad_bp
from .facultad_resource import facultad_bp
from .autoridad_resource import autoridad_bp
from .departamento_resource import departamento_bp
from .cargo_resource import cargo_bp
from .alumno_resource import alumno_bp
from .grado_resource import grado_bp
from .tipo_dedicacion_resource import tipo_dedicacion_bp
from .tipo_especialidad_resource import tipo_especialidad_bp
from .tipo_documento_resource import tipo_documento_bp
from .plan_resource import plan_bp
from .orientacion_resource import orientacion_bp
from .especialidad_resource import especialidad_bp
from .categoria_cargo_resource import categoria_cargo_bp
from .materia_resource import materia_bp
from .certificado_resource import certificado_bp
all_blueprints = [
    alumno_bp,
    # universidad_bp,  # Agrégalo aquí si lo descomentaste arriba
]