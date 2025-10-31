from dataclasses import dataclass
from app import db


@dataclass
class TipoDedicacion(db.Model):
    __tablename__ = 'tipos_dedicacion'
    nombre: str = db.Column(db.String(100))
    observacion: str = db.Column(db.String(100), nullable=True)
    id_tipo_dedicacion: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    #Relacion
    cargos = db.relationship('Cargo', back_populates='tipo_dedicacion', lazy='dynamic')