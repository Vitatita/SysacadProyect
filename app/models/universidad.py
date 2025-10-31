from dataclasses import dataclass
from app import db

@dataclass
class Universidad(db.Model):
    __tablename__ = 'universidades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    sigla = db.Column(db.String(100), nullable=False, unique=True)
    tipo = db.Column(db.String(20), nullable=False)
    #Relaciones
    facultades = db.relationship("Facultad", back_populates="universidad_rel")
    alumnos = db.relationship('Alumno', back_populates='universidad_rel')