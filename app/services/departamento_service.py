from app.models import Departamento
from app.repositories import DepartamentoRepository
from app import db, cache

class DepartamentoService:
  @staticmethod
  def crear_departamento(departamento: Departamento) -> Departamento:
    nuevo_departamento = DepartamentoRepository.crear_departamento(departamento)
    cache.delete("departamentos_todos")
    cache.delete(f"departamento_{nuevo_departamento.id}")
    return nuevo_departamento

  @staticmethod
  def buscar_por_id(id: int) -> Departamento | None:
    cache_key = f"departamento_{id}"
    departamento = cache.get(cache_key)
    if not departamento:
      departamento = DepartamentoRepository.buscar_por_id(id)
      cache.set(cache_key, departamento)
    return departamento

  @staticmethod
  def buscar_todos() -> list[Departamento]:
    departamentos = cache.get("departamentos_todos")
    if not departamentos:
      departamentos = DepartamentoRepository.obtener_todos_los_departamentos()
      cache.set("departamentos_todos", departamentos, timeout=60)
    return departamentos

  @staticmethod
  def actualizar_departamento(departamento: Departamento, id: int) -> Departamento | None:
    resultado = DepartamentoRepository.actualizar_departamento(departamento, id)
    cache.delete(f"departamento_{id}")
    cache.delete("departamentos_todos")
    return resultado

  @staticmethod
  def eliminar_departamento(id: int) -> bool:
    resultado = DepartamentoRepository.eliminar_departamento(id)
    cache.delete(f"departamento_{id}")
    cache.delete("departamentos_todos")
    return resultado
