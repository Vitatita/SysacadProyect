from dataclasses import dataclass
from app import db

@dataclass
class Autoridad(db.Model):
    __tablename__ = 'autoridades'
    autoridad_id: int = db.Column(db.Integer, primary_key=True)  # Clave primaria única
    nombre: str = db.Column(db.String(100), nullable=False)
    cargo: str = db.Column(db.String(100), nullable=False)
    telefono: str = db.Column(db.String(20), nullable=False)
    email: str = db.Column(db.String(100), nullable=False, unique=True)
    id_facultad: int = db.Column(db.Integer, db.ForeignKey('facultades.id'), nullable=False)
    facultad = db.relationship('Facultad', back_populates='autoridades')