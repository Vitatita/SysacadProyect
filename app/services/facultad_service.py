from app.models import Facultad
from app.repositories.facultad_repositorio import FacultadRepository
from app import db, cache
class FacultadService:

  @staticmethod
  def crear(facultad: Facultad) -> Facultad:
    nueva_facultad = FacultadRepository.crear(facultad)
    cache.delete("facultades_todas")
    cache.delete(f"facultad_{nueva_facultad.id}")
    return nueva_facultad

  def buscar_por_id(id: int) -> Facultad | None:
    cache_key = f"facultad_{id}"
    facultad = cache.get(cache_key)
    if not facultad:
      facultad = FacultadRepository.buscar_por_id(id)
      cache.set(cache_key, facultad, timeout=60)
    return facultad
  
  def buscar_todos() -> list[Facultad]:
    facultades = cache.get("facultades_todas")
    if not facultades:
      facultades = FacultadRepository.buscar_todos()
      cache.set("facultades_todas", facultades, timeout=60)
    return facultades
    
  def actualizar(facultad: Facultad, id: int) -> Facultad | None:
    resultado = FacultadRepository.actualizar(facultad, id)
    cache.delete(f"facultad_{id}")
    cache.delete("facultades_todas")
    return resultado
  
  def borrar_por_id(id: int) -> bool:
    resultado = FacultadRepository.borrar_por_id(id)
    cache.delete(f"facultad_{id}")
    cache.delete("facultades_todas")
    return resultado