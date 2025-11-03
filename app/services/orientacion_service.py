from app.models import Orientacion
from app.repositories.orientacion_repositorio import OrientacionRepository
from app import db, cache

class OrientacionService:
  @staticmethod
  def crear(orientacion: Orientacion) -> Orientacion:
    nuevo_orientacion = OrientacionRepository.crear(orientacion)
    cache.delete("orientaciones_todas")
    cache.delete(f"orientacion_{nuevo_orientacion.id}")
    return nuevo_orientacion

  @staticmethod
  def buscar_por_id(id: int) -> Orientacion | None:
    cache_key = f"orientacion_{id}"
    orientacion = cache.get(cache_key)
    if not orientacion:
      orientacion = OrientacionRepository.buscar_por_id(id)
      cache.set(cache_key, orientacion, timeout=60)
    return orientacion
  
  @staticmethod
  def buscar_todos() -> list[Orientacion]:
    orientaciones = cache.get("orientaciones_todas")
    if not orientaciones:
      orientaciones = OrientacionRepository.buscar_todos()
      cache.set("orientaciones_todas", orientaciones, timeout=60)
    return orientaciones
    
  @staticmethod
  def actualizar(orientacion: Orientacion, id: int) -> Orientacion | None:
    resultado = OrientacionRepository.actualizar(orientacion, id)
    cache.delete(f"orientacion_{id}")
    cache.delete("orientaciones_todas")
    return resultado
  
  @staticmethod
  def borrar_por_id(id: int) -> bool:
    resultado = OrientacionRepository.borrar_por_id(id)
    cache.delete(f"orientacion_{id}")
    cache.delete("orientaciones_todas")
    return resultado