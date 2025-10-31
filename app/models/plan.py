from dataclasses import dataclass
from app import db

@dataclass
class Plan(db.Model):
    __tablename__ = 'planes'

    id_plan: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    fecha_inicio: db.Column = db.Column(db.Date, nullable=False)
    fecha_fin: db.Column = db.Column(db.Date, nullable=False)
    observacion: str = db.Column(db.String(100), nullable=True)
    id_orientacion: int = db.Column(db.Integer, db.ForeignKey('orientaciones.id_orientacion'), nullable=False)

    orientacion = db.relationship('Orientacion', back_populates='planes')