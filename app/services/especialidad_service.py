from app.models import Especialidad, especialidad
from app.repositories import EspecialidadRepository
from app import db, cache

class EspecialidadService:

    @staticmethod
    def crear_especialidad(especialidad: Especialidad) -> Especialidad:
        nueva_especialidad = EspecialidadRepository.crear_especialidad(especialidad)
        cache.delete("especialidades_todas")
        cache.delete(f"especialidad_{nueva_especialidad.id}")
        return nueva_especialidad

    @staticmethod
    def buscar_por_id(id: int) -> Especialidad | None:
        cache_key = f"especialidad_{id}"
        especialidad = cache.get(cache_key)
        if not especialidad:
            especialidad = EspecialidadRepository.buscar_por_id(id)
            cache.set(cache_key, especialidad)
        return especialidad

    @staticmethod
    def buscar_todas() -> list[Especialidad]:
        especialidades = cache.get("especialidades_todas")
        if not especialidades:
            especialidades = EspecialidadRepository.buscar_todas()
            cache.set("especialidades_todas", especialidades, timeout=60)
        return especialidades

    @staticmethod
    def actualizar_especialidad(id: int, especialidad: Especialidad) -> Especialidad | None:
        resultado = EspecialidadRepository.actualizar_especialidad(id, especialidad)
        cache.delete(f"especialidad_{id}")
        cache.delete("especialidades_todas")
        return resultado

    @staticmethod
    def eliminar_especialidad(id: int) -> bool:
        resultado = EspecialidadRepository.eliminar_especialidad(id)
        cache.delete(f"especialidad_{id}")
        cache.delete("especialidades_todas")
        return resultado