from app import db
from app.models import Autoridad

class AutoridadRepository:
    @staticmethod
    def crear_autoridad(autoridad) -> Autoridad:
        """Crea una nueva autoridad en la base de datos"""
        db.session.add(autoridad)
        db.session.commit()
        return autoridad
    
    @staticmethod
    def buscar_todos() -> list[Autoridad]:
        """Obtiene todas las autoridades"""
        return Autoridad.query.all()
    
    @staticmethod
    def buscar_por_id(autoridad_id) -> Autoridad | None:
        """Obtiene una autoridad por su ID"""
        return Autoridad.query.get(autoridad_id)
    
    @staticmethod
    def actualizar_autoridad(autoridad_id, autoridad) -> Autoridad | None:
        """Actualiza una autoridad existente"""
        existing_autoridad = AutoridadRepository.buscar_por_id(autoridad_id)
        if existing_autoridad:
            existing_autoridad.nombre = autoridad.nombre
            existing_autoridad.descripcion = autoridad.descripcion
            db.session.commit()
            return existing_autoridad
        return None
    
    #revisar actualizar_autoridad 
    
    @staticmethod
    def borrar_por_id(autoridad_id) -> bool:
        """Elimina una autoridad por su ID"""
        autoridad = AutoridadRepository.buscar_por_id(autoridad_id)
        if autoridad:
            db.session.delete(autoridad)
            db.session.commit()
            return True
        return False