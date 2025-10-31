from dataclasses import dataclass
from app import db

@dataclass
class Facultad(db.Model):
    __tablename__ = 'facultades'
    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    abreviatura: str = db.Column(db.String(10), nullable=False, unique=True)
    directorio: str = db.Column(db.String(100), nullable=True)
    sigla: str = db.Column(db.String(10), nullable=False, unique=True)
    codigoPostal: str = db.Column(db.String(10), nullable=True)
    ciudad: str = db.Column(db.String(100), nullable=True)
    domicilio: str = db.Column(db.String(100), nullable=True)
    telefono: str = db.Column(db.String(20), nullable=True)
    contacto: str = db.Column(db.String(100), nullable=True)
    email: str = db.Column(db.String(100), nullable=True)
    id_universidad = db.Column(db.Integer, db.ForeignKey('universidades.id'), nullable=False)


    autoridades = db.relationship('Autoridad', back_populates='facultad')
    departamentos = db.relationship('Departamento', back_populates='facultad')
    universidad_rel = db.relationship('Universidad', back_populates='facultades', foreign_keys=[id_universidad])
    