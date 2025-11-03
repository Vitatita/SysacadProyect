from app.models import Universidad
from app.repositories.universidad_repositorio import UniversidadRepository
class UniversidadService:

  @staticmethod
  def crear_universidad(universidad: Universidad) -> Universidad:
    UniversidadRepository.crear_universidad(universidad)
    return universidad

  def buscar_todos() -> list[Universidad]:
    universidades = UniversidadRepository.buscar_todos()
    return universidades

  def buscar_por_id(id: int) -> Universidad | None:
    universidad = UniversidadRepository.buscar_por_id(id)
    return universidad
    
  def actualizar_universidad(universidad: Universidad, id: int) -> Universidad | None:
    UniversidadRepository.actualizar(universidad, id)
    return universidad
  
  def borrar_universidad(id: int) -> bool:
    universidad= UniversidadRepository.borrar_universidad(id)
    return universidad