from app.models import Materia
from app.repositories.materia_repositorio import MateriaRepository
from app import db, cache
class MateriaService:
    
    @staticmethod
    def crear(materia: Materia) -> Materia:
        nuevo_materia = MateriaRepository.crear(materia)
        cache.delete("materias_todas")
        cache.delete(f"materia_{nuevo_materia.id}")
        return nuevo_materia
    
    @staticmethod
    def buscar_por_id(id: int) -> Materia | None:
        cache_key = f"materia_{id}"
        materia = cache.get(cache_key)
        if not materia:
            materia = MateriaRepository.buscar_por_id(id)
            cache.set(cache_key, materia, timeout=60)
        return materia
    
    @staticmethod
    def buscar_todos() -> list[Materia]:
        materias = cache.get("materias_todas")
        if not materias:
            materias = MateriaRepository.buscar_todos()
            cache.set("materias_todas", materias, timeout=60)
        return materias

    @staticmethod
    def actualizar( id: int,materia: Materia) -> Materia | None:
        resultado = MateriaRepository.actualizar(id,materia)
        cache.delete(f"materia_{id}")
        cache.delete("materias_todas")
        return resultado

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        resultado = MateriaRepository.borrar(id)
        cache.delete(f"materia_{id}")
        cache.delete("materias_todas")
        return bool(resultado)