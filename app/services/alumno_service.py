import csv
import io
from datetime import datetime
from app import db
from app.models.alumno import Alumno
from app.utils.retry import retry  # Asegúrate de tener el archivo app/utils/retry.py

class AlumnoService:
    
    @staticmethod
    def importar_archivo_txt(archivo):
        """
        Lee el archivo ALUMNOS.TXT, parsea los datos y los guarda.
        Esta es la función que te faltaba.
        """
        # 1. Decodificar bytes a string
        stream = io.StringIO(archivo.read().decode("utf-8"), newline=None)
        csv_reader = csv.reader(stream, delimiter=',') 

        procesados = 0
        errores = 0
        lista_errores = []

        for row in csv_reader:
            try:
                # Parsear fecha si existe (columna 4)
                fecha_nac = None
                if len(row) > 4 and row[4]:
                    try:
                        fecha_nac = datetime.strptime(row[4], '%d/%m/%Y').date()
                    except ValueError:
                        pass 

                # Crear objeto Alumno
                nuevo_alumno = Alumno(
                    facultad_id=int(row[0]),
                    tipo_documento=int(row[1]),
                    nro_documento=int(row[2]),
                    nombre_completo=row[3], 
                    fecha_nacimiento=fecha_nac,
                    sexo=row[5],
                    nro_legajo=int(row[6]) if len(row) > 6 and row[6] else None
                )

                # Guardar con Retry
                AlumnoService.guardar_con_retry(nuevo_alumno)
                procesados += 1
            
            except Exception as e:
                errores += 1
                lista_errores.append(f"Fila {procesados+errores}: {str(e)}")

        return {
            "estado": "Procesado",
            "total_guardados": procesados, 
            "total_fallidos": errores, 
            "detalle_errores": lista_errores
        }

    @staticmethod
    @retry(max_attempts=3, delay=1.0)
    def guardar_con_retry(alumno):
        db.session.add(alumno)
        db.session.commit()