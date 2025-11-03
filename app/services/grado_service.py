from app.models import Grado
from app.repositories.grado_repositorio import GradoRepository
from app import db, cache

class GradoService:
  @staticmethod
  def crear(grado: Grado) -> Grado:
    nuevo_grado = GradoRepository.crear(grado)
    cache.delete("grados_todos")
    cache.delete(f"grado_{nuevo_grado.id}")
    return nuevo_grado

  def buscar_por_id(id: int) -> Grado | None:
    cache_key = f"grado_{id}"
    grado = cache.get(cache_key)
    if not grado:
      grado = GradoRepository.buscar_por_id(id)
      cache.set(cache_key, grado, timeout=60)
    return grado
    
  def buscar_todos() -> list[Grado]:
    grados = cache.get("grados_todos")
    if not grados:
      grados = GradoRepository.buscar_todos()
      cache.set("grados_todos", grados, timeout=60)
    return grados

  def actualizar(grado: Grado, id: int) -> Grado | None:
    resultado = GradoRepository.actualizar(grado, id)
    cache.delete(f"grado_{id}")
    cache.delete("grados_todos")
    return resultado
  
  def borrar_por_id(id: int) -> bool:
    resultado = GradoRepository.borrar_por_id(id)
    cache.delete(f"grado_{id}")
    cache.delete("grados_todos")
    return resultado