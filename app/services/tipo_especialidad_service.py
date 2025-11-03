from app.models import TipoEspecialidad
from app.repositories.tipo_especialidad_repositorio import TipoEspecialidadRepository
from app import db, cache

class TipoEspecialidadService:

    @staticmethod
    def crear_tipo_especialidad(tipoespecialidad: TipoEspecialidad) -> TipoEspecialidad:
        nuevo_tipoespecialidad = TipoEspecialidadRepository.crear_tipo_especialidad(tipoespecialidad)
        cache.delete("tipos_especialidad_todos")
        cache.delete(f"tipo_especialidad_{nuevo_tipoespecialidad.id}")
        return nuevo_tipoespecialidad

    @staticmethod
    def buscar_por_id(id: int) -> TipoEspecialidad | None:
        cache_key = f"tipo_especialidad_{id}"
        tipoespecialidad = cache.get(cache_key)
        if not tipoespecialidad:
            tipoespecialidad = TipoEspecialidadRepository.buscar_por_id(id)
            cache.set(cache_key, tipoespecialidad, timeout=60)
        return tipoespecialidad

    @staticmethod
    def buscar_todos() -> list[TipoEspecialidad]:
        cache_key = "tipos_especialidad_todos"
        tipos_especialidad = cache.get(cache_key)
        if not tipos_especialidad:
            tipos_especialidad = TipoEspecialidadRepository.buscar_todos()
            cache.set(cache_key, tipos_especialidad, timeout=60)
        return tipos_especialidad

    @staticmethod
    def actualizar_tipo_especialidad(tipoespecialidad: TipoEspecialidad, id: int) -> TipoEspecialidad | None:
        resultado = TipoEspecialidadRepository.actualizar(tipoespecialidad, id)
        cache.delete(f"tipo_especialidad_{id}")
        cache.delete("tipos_especialidad_todos")
        return resultado

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        resultado = TipoEspecialidadRepository.borrar_por_id(id)
        cache.delete(f"tipo_especialidad_{id}")
        cache.delete("tipos_especialidad_todos")
        return resultado