from dataclasses import dataclass
from app import db

@dataclass
class Orientacion(db.Model):
    __tablename__ = 'orientaciones'

    id_orientacion: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    plan_nombre: str = db.Column(db.String(100), nullable=False)  # Opcional, si querés guardar nombre de plan directamente (puede sacarse)
    # materia: str = db.Column(db.String(100))  # Si no lo usás, podés sacarlo

    materias = db.relationship('Materia', back_populates='orientacion', lazy='dynamic')
    planes = db.relationship('Plan', back_populates='orientacion', lazy='dynamic')
    especialidades = db.relationship('Especialidad', back_populates='orientacion', lazy='dynamic')
