import time
import logging
from functools import wraps

# Configuración básica de logs para ver en la terminal los intentos
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorador para reintentar una operación si falla (Backoff Exponencial).
    
    Args:
        max_attempts (int): Número máximo de intentos (default 3).
        delay (float): Tiempo de espera inicial en segundos (default 1.0).
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    # Intenta ejecutar la función original
                    return func(*args, **kwargs)
                
                except Exception as e:
                    # Si falla, entramos aquí
                    if attempt == max_attempts:
                        # Si era el último intento, registramos error y lanzamos la excepción real
                        logger.error(f"Falló definitivamente '{func.__name__}' después de {max_attempts} intentos. Error: {e}")
                        raise e
                    
                    # Cálculo matemático del tiempo de espera (1s, 2s, 4s...)
                    wait_time = delay * (2 ** (attempt - 1))
                    
                    logger.warning(f"Intento {attempt} falló en '{func.__name__}'. Reintentando en {wait_time}s... Error: {e}")
                    
                    # Esperamos antes del siguiente intento
                    time.sleep(wait_time)
                    attempt += 1
        return wrapper
    return decorator