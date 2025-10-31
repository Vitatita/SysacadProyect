from dataclasses import dataclass
from app import db

@dataclass
class Especialidad(db.Model):
    __tablename__ = 'especialidades'

    id_especialidad: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    letra: str = db.Column(db.String(1), nullable=False)
    observacion: str = db.Column(db.String(100), nullable=True)

    id_orientacion = db.Column(db.Integer, db.ForeignKey('orientaciones.id_orientacion'), nullable=False)
    id_grado = db.Column(db.String(100), db.ForeignKey('grados.nombre'), nullable=False)
    id_grado_sigla = db.Column(db.String(10), db.ForeignKey('grados.sigla'), nullable=False)
    id_tipo_especialidad = db.Column(db.Integer, db.ForeignKey('tipos_especialidad.id_tipo_especialidad'), nullable=False)

    orientacion = db.relationship('Orientacion', back_populates='especialidades')
    tipo_especialidad = db.relationship(
        'TipoEspecialidad',
        back_populates='especialidades',
        foreign_keys=[id_tipo_especialidad]
    )

