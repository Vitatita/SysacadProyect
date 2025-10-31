from app import db
from app.models import Departamento

class DepartamentoRepository:
    """Repositorio para la entidad Departamento."""

    @staticmethod
    def crear(departamento: Departamento) -> Departamento:
        db.session.add(departamento)
        db.session.commit()
        return departamento

    @staticmethod
    def buscar_por_id(id_departamento: int) -> Departamento | None:
        return Departamento.query.get(id_departamento)

    @staticmethod
    def buscar_todos() -> list[Departamento]:
        return Departamento.query.all()

    @staticmethod
    def actualizar(departamento: Departamento) -> Departamento | None:
        departamento_existente = db.session.merge(departamento)
        db.session.commit()
        return departamento_existente

    @staticmethod
    def borrar_por_id(id_departamento: int) -> bool:
        departamento = Departamento.query.get(id_departamento)
        if not departamento:
            return None
        db.session.delete(departamento)
        db.session.commit()
        return departamento