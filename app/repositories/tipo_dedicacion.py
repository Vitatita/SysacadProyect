from app import db
from app.models import TipoDedicacion

class TipoDedicacionRepository:
    """Repositorio para la entidad TipoDedicacion"""

    @staticmethod
    def crear(tipo_dedicacion: TipoDedicacion) -> TipoDedicacion:
        db.session.add(tipo_dedicacion)
        db.session.commit()
        return tipo_dedicacion

    @staticmethod
    def buscar_por_id(id_tipo: int) -> TipoDedicacion | None:
        return TipoDedicacion.query.get(id_tipo)

    @staticmethod
    def buscar_todos() -> list[TipoDedicacion]:
        return TipoDedicacion.query.all()

    @staticmethod
    def actualizar(tipo_dedicacion: TipoDedicacion) -> TipoDedicacion | None:
        tipo_existente = db.session.merge(tipo_dedicacion)
        db.session.commit()
        return tipo_existente

    @staticmethod
    def borrar_por_id(id_tipo: int) -> bool:
        tipo_dedicacion = TipoDedicacion.query.get(id_tipo)
        if not tipo_dedicacion:
            return None
        db.session.delete(tipo_dedicacion)
        db.session.commit()
        return tipo_dedicacion