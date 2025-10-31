from dataclasses import dataclass
from app import db

@dataclass
class Materia(db.Model):
    __tablename__ = 'materias'

    id_materia: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    codigo: str = db.Column(db.String(20), nullable=False)
    observacion: str = db.Column(db.String(100), nullable=True)
    id_orientacion: int = db.Column(db.Integer, db.ForeignKey('orientaciones.id_orientacion'), nullable=False)

    orientacion = db.relationship('Orientacion', back_populates='materias')