from app import db
from app.models import Facultad

class FacultadRepository:
    """Repositorio para la entidad Facultad."""

    @staticmethod
    def crear(facultad: Facultad) -> Facultad:
        db.session.add(facultad)
        db.session.commit()
        return facultad

    @staticmethod
    def buscar_por_id(id_facultad: int) -> Facultad | None:
        return Facultad.query.get(id_facultad)

    @staticmethod
    def buscar_todos() -> list[Facultad]:
        return Facultad.query.all()

    @staticmethod
    def actualizar(facultad: Facultad) -> Facultad | None:
        facultad_existente = db.session.merge(facultad)
        db.session.commit()
        return facultad_existente

    @staticmethod
    def borrar_por_id(id_facultad: int) -> bool:
        facultad = Facultad.query.get(id_facultad)
        if not facultad:
            return None
        db.session.delete(facultad)
        db.session.commit()
        return facultad