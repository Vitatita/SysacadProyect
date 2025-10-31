from app import db
from app.models.tipo_especialidad import TipoEspecialidad

class TipoEspecialidadRepository:

    @staticmethod
    def crear(tipo_especialidad: TipoEspecialidad) -> TipoEspecialidad:
        db.session.add(tipo_especialidad)
        db.session.commit()
        return tipo_especialidad

    @staticmethod
    def buscar_por_id(id_tipo: int) -> TipoEspecialidad | None:
        return TipoEspecialidad.query.get(id_tipo)

    @staticmethod
    def buscar_todos() -> list[TipoEspecialidad]:
        return TipoEspecialidad.query.all()

    @staticmethod
    def actualizar(tipo_especialidad: TipoEspecialidad) -> TipoEspecialidad | None:
        tipo_existente = db.session.merge(tipo_especialidad)
        db.session.commit()
        return tipo_existente

    @staticmethod
    def borrar_por_id(id_tipo: int) -> bool:
        tipo_especialidad = TipoEspecialidad.query.get(id_tipo)
        if not tipo_especialidad:
            return None
        db.session.delete(tipo_especialidad)
        db.session.commit()
        return tipo_especialidad
