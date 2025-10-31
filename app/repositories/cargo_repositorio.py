from app import db
from app.models.cargo import Cargo

class CargoRepository:
    """"
    clase de repositorio para la entidad cargo.
    """
    @staticmethod
    def crear(cargo: Cargo) -> Cargo:
        db.session.add(cargo)
        db.session.commit()
        return cargo

    @staticmethod
    def buscar_por_nombre(nombre: str) -> Cargo | None:
        return Cargo.query.filter_by(nombre=nombre).first()

    @staticmethod
    def listar_cargo() -> list[Cargo]:
        return Cargo.query.all()

    @staticmethod
    def actualizar_cargo(cargo: Cargo) -> Cargo | None:
        cargo_existente = db.session.merge(cargo)
        if not cargo_existente:
            return None
        return cargo_existente

    @staticmethod
    def borrar_por_nombre(nombre: str) -> bool:
        cargo = Cargo.query.filter_by(nombre=nombre).first()
        if not cargo:
            return False
        db.session.delete(cargo)
        db.session.commit()
        return True