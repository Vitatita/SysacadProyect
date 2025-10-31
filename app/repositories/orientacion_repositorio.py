from app import db
from app.models import Orientacion

class OrientacionRepository:
    """
    Clase de repositorio para la entidad Orientacion.
    """

    @staticmethod
    def crear(orientacion: Orientacion) -> Orientacion:
        db.session.add(orientacion)
        db.session.commit()
        return orientacion

    @staticmethod
    def buscar_por_id(id_orientacion: int) -> Orientacion | None:
        return Orientacion.query.get(id_orientacion)

    @staticmethod
    def buscar_todas() -> list[Orientacion]:
        return Orientacion.query.all()

    @staticmethod
    def actualizar(orientacion: Orientacion) -> Orientacion | None:
        orientacion_existente = db.session.merge(orientacion)
        db.session.commit()
        return orientacion_existente

    @staticmethod
    def borrar_por_id(id_orientacion: int) -> bool:
        orientacion = Orientacion.query.get(id_orientacion)
        if not orientacion:
            return None
        db.session.delete(orientacion)
        db.session.commit()
        return orientacion
