from app import db
from app.models import CategoriaCargo

class CategoriaCargoRepository:
    """
    Clase de repositorio para la entidad CategoriaCargo.
    """
    @staticmethod
    def crear(categoria_cargo: CategoriaCargo) -> CategoriaCargo:
        db.session.add(categoria_cargo)
        db.session.commit()
        return categoria_cargo

    @staticmethod
    def buscar_por_id(id_categoria: int) -> CategoriaCargo | None:
        return CategoriaCargo.query.get(id_categoria)

    @staticmethod
    def buscar_todos() -> list[CategoriaCargo]:
        return CategoriaCargo.query.all()

    @staticmethod
    def actualizar(categoria_cargo: CategoriaCargo) -> CategoriaCargo | None:
        """
        Actualiza una categoría de cargo existente.
        merge() devuelve la instancia que está vinculada a la sesión.
        """
        categoria_existente = db.session.merge(categoria_cargo)
        db.session.commit()
        return categoria_existente
    @staticmethod
    def borrar_por_id(id_categoria: int) -> bool:
        categoria_cargo = CategoriaCargo.query.get(id_categoria)
        if not categoria_cargo:
            return None
        db.session.delete(categoria_cargo)
        db.session.commit()
        return categoria_cargo