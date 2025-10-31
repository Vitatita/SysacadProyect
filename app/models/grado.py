from dataclasses import dataclass
from app import db

@dataclass
class Grado(db.Model):
    __tablename__ = 'grados'

    id_grado: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False, unique=True)
    sigla: str = db.Column(db.String(10), nullable=False, unique=True)
    duracion: int = db.Column(db.Integer, nullable=False)
