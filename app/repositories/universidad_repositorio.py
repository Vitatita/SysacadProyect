from app import db
from app.models.universidad import Universidad

class UniversidadRepository:
    """
    Clase de repositorio para la entidad Universidad.
    """
    @staticmethod
    def crear_universidad(universidad: Universidad) -> Universidad:
        """
        Crea una nueva universidad en la base de datos.
        :param universidad: Objeto Universidad a crear.
        :return: Objeto Universidad creado.
        """
        db.session.add(Universidad)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int) -> Universidad | None:
        """
        Busca una universidad por su ID.
        :param id: ID de la universidad a buscar.
        :return: Objeto Universidad encontrado o None si no se encuentra.
        """
        return Universidad.query.get(id)

    @staticmethod
    def buscar_todos() -> list[Universidad]:
        """
        Busca todas las universidades en la base de datos.
        :return: Lista de objetos Universidad.
        """
        return Universidad.query.all()

    @staticmethod
    def actualizar(universidad: Universidad) -> Universidad | None:
        """
        Actualiza una universidad existente en la base de datos.
        :param id: ID de la universidad a actualizar.
        :param universidad: Objeto Universidad con los nuevos datos.
        :return: Objeto Universidad actualizado o None si no se encuentra.
        """
        universidad_existente = db.session.merge(universidad)
        db.session.commit()
        return universidad_existente

    @staticmethod
    def borrar_universidad(id: int) -> bool:
        """
        Borra una universidad por su ID.
        :param id: ID de la universidad a borrar.
        :return: True si se borró correctamente, False si no se encontró.
        """
        universidad = Universidad.query.get(id)
        if not universidad:
            return None
        db.session.delete(universidad)
        db.session.commit()
        return universidad