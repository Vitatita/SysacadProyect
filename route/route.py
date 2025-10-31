from flask import Flask

class RouteApp:
    def init_app(self, app: Flask) -> None:
        from app.resources import (alumno_bp, autoridad_bp, cargo_bp, categoria_cargo_bp, 
                                departamento_bp, especialidad_bp, facultad_bp, grado_bp, home_bp, 
                                materia_bp, orientacion_bp, plan_bp, tipo_dedicacion_bp, tipo_documento_bp,
                                tipo_especialidad_bp, universidad_bp, certificado_bp, ficha_alumno_bp)
        app.register_blueprint(alumno_bp, url_prefix='/api/alumnos')
        app.register_blueprint(autoridad_bp, url_prefix='/api/autoridades')
        app.register_blueprint(cargo_bp, url_prefix='/api/cargos')
        app.register_blueprint(categoria_cargo_bp, url_prefix='/api/categoria-cargos')
        app.register_blueprint(departamento_bp, url_prefix='/api/departamentos')
        app.register_blueprint(especialidad_bp, url_prefix='/api/especialidades')
        app.register_blueprint(facultad_bp, url_prefix='/api/facultades')
        app.register_blueprint(grado_bp, url_prefix='/api/grados')
        app.register_blueprint(home_bp, url_prefix='/api/home')
        app.register_blueprint(materia_bp, url_prefix='/api/materias')
        app.register_blueprint(orientacion_bp, url_prefix='/api/orientaciones')
        app.register_blueprint(plan_bp, url_prefix='/api/planes')
        app.register_blueprint(tipo_dedicacion_bp, url_prefix='/api/tipos-dedicacion')
        app.register_blueprint(tipo_documento_bp, url_prefix='/api/tipos-documento')
        app.register_blueprint(tipo_especialidad_bp, url_prefix='/api/tipos-especialidad')
        app.register_blueprint(universidad_bp, url_prefix='/api/universidades')
        app.register_blueprint(certificado_bp, url_prefix='/api/certificados')
        app.register_blueprint(ficha_alumno_bp, url_prefix='/api/fichas-alumno')
