from app.models import CategoriaCargo
from app.repositories import CategoriaCargoRepository
from app import db, cache

class CategoriaCargoService: #Aca se aplica **SRP, esta clase se encarga de la
    #logica de negocio para las categorias de cargo + cache**

    @staticmethod
    def crear_categoria_cargo(categoria_cargo: CategoriaCargo):
        nueva_categoria_cargo = CategoriaCargoRepository.crear_categoria_cargo(categoria_cargo) #Aca aplica DIP, ya que depende de cargorepository y no directamente
        cache.delete("categorias_cargo_todas")
        cache.delete(f"categoria_cargo_{nueva_categoria_cargo.id}")
        return nueva_categoria_cargo

    @staticmethod
    def buscar_por_id(id: int) -> CategoriaCargo | None:
        cache_key = f"categoria_cargo_{id}"
        categoria_cargo = cache.get(cache_key) 
        if categoria_cargo is None:
            categoria_cargo = CategoriaCargoRepository.buscar_por_id(id)
            cache.set(cache_key, categoria_cargo, timeout=60)
        return categoria_cargo

    @staticmethod
    def buscar_todos() -> list[CategoriaCargo]:
        categorias_cargo = cache.get("categorias_cargo_todas")
        if categorias_cargo is None:
            categorias_cargo = CategoriaCargoRepository.buscar_todos()
            cache.set("categorias_cargo_todas", categorias_cargo, timeout=60)
        return categorias_cargo

    @staticmethod
    def actualizar_categoria_cargo(id: int, categoria_cargo: CategoriaCargo) -> CategoriaCargo | None:
        resultado = CategoriaCargoRepository.actualizar_categoria_cargo(id, categoria_cargo)
        cache.delete(f"categoria_cargo_{id}")
        cache.delete("categorias_cargo_todas")
        return resultado

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        resultado = CategoriaCargoRepository.borrar_por_id(id)
        cache.delete(f"categoria_cargo_{id}")
        cache.delete("categorias_cargo_todas")
        return resultado