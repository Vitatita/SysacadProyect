from dataclasses import dataclass
from app import db

@dataclass
class Cargo(db.Model):
    __tablename__ = 'cargos'
    nombre: str = db.Column(db.String(100), primary_key=True)
    puntos: int = db.Column(db.Integer, nullable=False)
    id_categoria: int = db.Column(db.Integer, db.ForeignKey('categorias_cargos.id_categoria'), nullable=False)
    id_tipo_dedicacion: str = db.Column(db.String(100), db.ForeignKey('tipos_dedicacion.nombre'), nullable=False)


    # Relaciones (deben estar dentro de la clase)
    categoria = db.relationship('CategoriaCargo', back_populates='cargos')
    tipo_dedicacion = db.relationship('TipoDedicacion', back_populates='cargos')