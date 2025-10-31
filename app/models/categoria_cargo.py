from dataclasses import dataclass
from app import db

@dataclass
class CategoriaCargo(db.Model):
    __tablename__ = 'categorias_cargos'

    id_categoria: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False, unique=True)

    # Relaciones
    cargos = db.relationship('Cargo', back_populates='categoria', lazy='dynamic')
