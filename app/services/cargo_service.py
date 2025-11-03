from app.repositories import CargoRepository
from app import db, cache
from app.models import Cargo

class CargoService:
    
    @staticmethod
    def crear_cargo(cargo: Cargo) -> Cargo: #Aplica SRP, esta clase se encarga de la logica de negocio para los cargos + cache
        nuevo_cargo = CargoRepository.crear_cargo(cargo) #Se aplica DIP, ya que depende de CargoRepository
        cache.delete("cargos_todos")
        cache.delete(f"cargo_{nuevo_cargo.id}")
        return nuevo_cargo

    @staticmethod
    def buscar_cargo_por_id(id: int) -> Cargo | None:
        cache_key = f"cargo_{id}"
        cargo = cache.get(cache_key) #Cumple KISS
        if cargo is None:
            cargo = CargoRepository.buscar_cargo_por_id(id)
            cache.set(cache_key, cargo, timeout=60)
        return cargo  #Cumple YAGNI

    @staticmethod
    def buscar_todos() -> list[Cargo]:
        cargos = cache.get("cargos_todos")
        if cargos is None:
            cargos = CargoRepository.listar_cargo()
            cache.set("cargos_todos", cargos, timeout=60)
        return cargos

    @staticmethod
    def actualizar_cargo(id: int, cargo: Cargo) -> Cargo | None:
        resultado = CargoRepository.actualizar_cargo(id, cargo)
        cache.delete(f"cargo_{id}")
        cache.delete("cargos_todos")
        return resultado

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        resultado = CargoRepository.borrar_por_id(id)
        cache.delete(f"cargo_{id}")
        cache.delete("cargos_todos")
        return resultado