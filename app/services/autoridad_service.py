from app.models import Autoridad
from app.repositories import AutoridadRepository
from app import db, cache

class AutoridadService:
    
    @staticmethod
    def crear_autoridad(autoridad: Autoridad) -> Autoridad:
        nueva_autoridad = AutoridadRepository.crear_autoridad(autoridad)
        cache.delete("autoridades_todas")
        cache.delete(f"autoridad_{nueva_autoridad.id}")
        return nueva_autoridad

    @staticmethod
    def buscar_todas() -> list[Autoridad]:
        autoridades = cache.get("autoridades_todas")
        if autoridades is None:
            autoridades = AutoridadRepository.buscar_todos()
            cache.set("autoridades_todas", autoridades, timeout=60)
        return autoridades

    @staticmethod
    def buscar_por_id(id: int) -> Autoridad | None:
        cache_key = f"autoridad_{id}"
        autoridad = cache.get(cache_key)
        if autoridad is None:
            autoridad = AutoridadRepository.buscar_por_id(id)
            cache.set(cache_key, autoridad, timeout=60)
        return autoridad

    @staticmethod
    def actualizar_autoridad(id: int, autoridad: Autoridad) -> Autoridad | None:
        resultado = AutoridadRepository.actualizar_autoridad(id, autoridad)
        cache.delete(f"autoridad_{id}")
        cache.delete("autoridades_todas")
        return resultado

    @staticmethod
    def borrar_autoridad(id: int) -> bool:
        resultado = AutoridadRepository.borrar_autoridad(id)
        cache.delete(f"autoridad_{id}")
        cache.delete("autoridades_todas")
        return resultado
