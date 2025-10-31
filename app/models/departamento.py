from dataclasses import dataclass
from app import db

@dataclass
class Departamento(db.Model):
    __tablename__ = 'departamentos'
    
    id_departamento: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    codigo: str = db.Column(db.String(20), nullable=False, unique=True)
    observacion: str = db.Column(db.String(100), nullable=True)
    id_facultad: int = db.Column(db.Integer, db.ForeignKey('facultades.id'), nullable=False)

    facultad = db.relationship('Facultad', back_populates='departamentos')