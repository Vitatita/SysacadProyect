from dataclasses import dataclass
from app import db

@dataclass
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    
    # ID interno (autoincremental, no viene en el TXT)
    alumno_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # --- CAMPOS OBLIGATORIOS SEGÚN DOCUMENTO SCDA ---
    # Campo 1: Facultad (Numérico)
    facultad_id: int = db.Column(db.Integer, nullable=False)
    
    # Campo 2: Tipo Doc (Numérico: 1=DNI, etc.)
    tipo_documento: int = db.Column(db.Integer, nullable=False)
    
    # Campo 3: Nro Documento (Numérico)
    nro_documento: int = db.Column(db.Integer, nullable=False, unique=True)
    
    # Campo 4: Apellido y Nombres (Junto, formato "Apellido, Nombres")
    nombre_completo: str = db.Column(db.String(150), nullable=False)
    
    # Campo 5: Fecha Nacimiento (Formato fecha real Date, no String)
    fecha_nacimiento: str = db.Column(db.Date, nullable=True)
    
    # Campo 6: Sexo ("M" o "F")
    sexo: str = db.Column(db.String(1), nullable=True)
    
    # Campo 7: Legajo (Numérico)
    nro_legajo: int = db.Column(db.Integer, nullable=True)

    # Puedes mantener tu relación con Universidad si es parte de tu TP anual, 
    # pero para el importador SCDA no es obligatorio recibirlo en el TXT.
    id_universidad = db.Column(db.Integer, db.ForeignKey('universidades.id'), nullable=True)