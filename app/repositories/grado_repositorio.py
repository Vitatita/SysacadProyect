from app import db
from app.models import Grado

class GradoRepository:

    @staticmethod
    def crear(grado: Grado) -> Grado:
        db.session.add(grado)
        db.session.commit()
        return grado

    @staticmethod
    def buscar_por_id(id_grado: int) -> Grado | None:
        return Grado.query.get(id_grado)

    @staticmethod
    def buscar_todos() -> list[Grado]:
        return Grado.query.all()

    @staticmethod
    def actualizar(grado: Grado) -> Grado | None:
        grado_existente = db.session.merge(grado)
        db.session.commit()
        return grado_existente

    @staticmethod
    def borrar_por_id(id_grado: int) -> bool:
        grado = Grado.query.get(id_grado)
        if not grado:
            return False
        db.session.delete(grado)
        db.session.commit()
        return True
