from app import cache

class CacheHelper:
    @staticmethod
    def limpiar_cache_entidad(nombre: str, id: int = None):
        cache.delete(f"{nombre}_todos")
        if id:
            cache.delete(f"{nombre}_{id}")
