from app import db
from app.models import Especialidad

class EspecialidadRepository:
    @staticmethod
    def crear(especialidad: Especialidad) -> Especialidad:
        db.session.add(especialidad)
        db.session.commit()
        return especialidad

    @staticmethod
    def buscar_por_id(id_especialidad: int) -> Especialidad | None:
        return Especialidad.query.get(id_especialidad)

    @staticmethod
    def buscar_todos() -> list[Especialidad] | None:
        return Especialidad.query.all()

    @staticmethod
    def actualizar(especialidad: Especialidad) -> Especialidad | None:
        especialidad_existente = db.session.merge(especialidad)
        db.session.commit()
        return especialidad_existente

    @staticmethod
    def borrar_por_id(id_especialidad: int) -> bool:
        especialidad = Especialidad.query.get(id_especialidad)
        if not especialidad:
            return None
        db.session.delete(especialidad)
        db.session.commit()
        return especialidad
