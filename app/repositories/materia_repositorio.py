from app import db
from app.models import Materia

class MateriaRepository:
    @staticmethod
    def crear(materia: Materia) -> Materia:
        db.session.add(materia)
        db.session.commit()
        return materia

    @staticmethod
    def buscar_por_id(id_materia: int) -> Materia | None:
        return Materia.query.get(id_materia)

    @staticmethod
    def buscar_todos() -> list[Materia]:
        return Materia.query.all()

    @staticmethod
    def actualizar(materia: Materia) -> Materia | None:
        materia_existente = db.session.merge(materia)
        db.session.commit()
        return materia_existente

    @staticmethod
    def borrar_por_id(id_materia: int) -> bool:
        materia = Materia.query.get(id_materia)
        if not materia:
            return None
        db.session.delete(materia)
        db.session.commit()
        return materia