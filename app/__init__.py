import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_caching import Cache
from hashids import Hashids

# Inicializamos las extensiones fuera de la función
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cache = Cache()

# Configuración básica de hashids
hashids = Hashids(salt="mi_secreto_examen", min_length=8)

def create_app():
    app = Flask(__name__)

    # --- 1. CONFIGURACIÓN DIRECTA (Para evitar errores de lectura) ---
    # Le decimos explícitamente dónde crear la base de datos local
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basedatos_local.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'clave_secreta_para_el_examen'
    app.config['CACHE_TYPE'] = 'SimpleCache'
    # ---------------------------------------------------------------

    # --- 2. INICIALIZAR EXTENSIONES CON LA APP YA CONFIGURADA ---
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cache.init_app(app)

    # --- 3. REGISTRAR TUS RUTAS (BLUEPRINTS) ---
    # Importamos aquí para evitar errores circulares
    from app.resources import all_blueprints
    
    for bp in all_blueprints:
        app.register_blueprint(bp, url_prefix="/api/v1")

    # Guardamos hashids en la app por si lo usas luego
    app.hashids = hashids

    return app
