from app.models import Plan
from app.repositories.plan_repositorio import PlanRepository
from app import db, cache
class PlanService:
  
  @staticmethod
  def crear(plan : Plan) -> Plan:
    nuevo_plan = PlanRepository.crear(plan)
    cache.delete("planes_todos")
    cache.delete(f"plan_{nuevo_plan.id}")
    return nuevo_plan
  
  @staticmethod
  def buscar_por_id(id: int) -> Plan | None:
    cache_key = f"plan_{id}"
    plan = cache.get(cache_key)
    if not plan:
      plan = PlanRepository.buscar_por_id(id)
      cache.set(cache_key, plan, timeout=60)
    return plan

  @staticmethod
  def buscar_todos() -> list[Plan]:
    planes = cache.get("planes_todos")
    if not planes:
      planes = PlanRepository.buscar_todos()
      cache.set("planes_todos", planes, timeout=60)
    return planes

  @staticmethod
  def actualizar_plan(id: int, plan: Plan) -> Plan | None:
    plan_existente = PlanRepository.buscar_por_id(id)
    if not plan_existente:
      return None
    # agregar Actualizar los campos del plan existente con los valores del nuevo plan
    plan_existente.nombre = plan.nombre
    plan_existente.descripcion = plan.descripcion
    plan_existente.creditos = plan.creditos
    db.session.commit()
    cache.delete(f"plan_{id}")
    cache.delete("planes_todos")
    return plan_existente

  @staticmethod
  def borrar_por_id(id: int) -> bool:
    resultado = PlanRepository.borrar_por_id(id)
    cache.delete(f"plan_{id}")
    cache.delete("planes_todos")
    return resultado