from app import db
from app.models.plan import Plan

class PlanRepository:
    @staticmethod
    def crear(plan: Plan) -> Plan:
        db.session.add(plan)
        db.session.commit()
        return plan

    @staticmethod
    def buscar_por_id(id_plan: int) -> Plan | None:
        return Plan.query.get(id_plan)

    @staticmethod
    def buscar_todos() -> list[Plan]:
        return Plan.query.all()

    @staticmethod
    def actualizar(plan: Plan) -> Plan | None:
        plan_existente = db.session.merge(plan)
        db.session.commit()
        return plan_existente

    @staticmethod
    def borrar_por_id(id_plan: int) -> bool:
        plan = Plan.query.get(id_plan)
        if not plan:
            return None
        db.session.delete(plan)
        db.session.commit()
        return plan