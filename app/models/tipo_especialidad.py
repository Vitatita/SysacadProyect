from dataclasses import dataclass
from app import db

@dataclass
class TipoEspecialidad(db.Model):
    __tablename__ = 'tipos_especialidad'

    id_tipo_especialidad: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)

    especialidades = db.relationship(
        'Especialidad',
        back_populates='tipo_especialidad'
    )