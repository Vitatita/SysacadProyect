from app.models import TipoDedicacion
from app.repositories.tipo_dedicacion import TipoDedicacionRepository
from app import db, cache
class TipoDedicacionService:
    
    @staticmethod
    def crear(tipo_dedicacion: TipoDedicacion) -> TipoDedicacion:
        nuevo_tipo_dedicacion = TipoDedicacionRepository.crear(tipo_dedicacion)
        cache.delete("tipos_dedicacion_todos")
        cache.delete(f"tipo_dedicacion_{nuevo_tipo_dedicacion.id}")
        return nuevo_tipo_dedicacion
    
    @staticmethod
    def buscar_por_id(id: int) -> TipoDedicacion | None:
        cache_key = f"tipo_dedicacion_{id}"
        tipo_dedicacion = cache.get(cache_key)
        if not tipo_dedicacion:
            tipo_dedicacion = TipoDedicacionRepository.buscar_por_id(id)
            cache.set(cache_key, tipo_dedicacion, timeout=60)
        return tipo_dedicacion
    
    @staticmethod
    def buscar_todos() -> list[TipoDedicacion]:
        cache_key = "tipos_dedicacion_todos"
        tipos_dedicacion = cache.get(cache_key)
        if not tipos_dedicacion:
            tipos_dedicacion = TipoDedicacionRepository.buscar_todos()
            cache.set(cache_key, tipos_dedicacion, timeout=60)
        return tipos_dedicacion

    @staticmethod
    def actualizar(id: int, tipo_dedicacion: TipoDedicacion) -> TipoDedicacion | None:
        resultado = TipoDedicacionRepository.actualizar(id, tipo_dedicacion)
        cache.delete(f"tipo_dedicacion_{id}")
        cache.delete("tipos_dedicacion_todos")
        return resultado

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        resultado = TipoDedicacionRepository.borrar_por_id(id)
        cache.delete(f"tipo_dedicacion_{id}")
        cache.delete("tipos_dedicacion_todos")
        return resultado