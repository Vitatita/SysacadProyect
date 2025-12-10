import csv
import io
from datetime import datetime
from app import db
from app.models.alumno import Alumno
from app.utils.retry import retry # Asegúrate de tener este archivo creado

class AlumnoService:
    # ... (Tus métodos CRUD actuales pueden quedarse si los necesitas) ...

    @staticmethod
    def importar_archivo_scda(archivo):
        """
        Lee el archivo ALUMNOS.TXT del SCDA y guarda los alumnos.
        """
        # Convertir bytes a string
        stream = io.StringIO(archivo.read().decode("utf-8"), newline=None)
        csv_reader = csv.reader(stream, delimiter=',') # SCDA separado por comas

        procesados = 0
        errores = 0
        
        for row in csv_reader:
            try:
                # Mapeo según orden de columnas SCDA:
                # row[0]=Facultad, row[1]=TipoDoc, row[2]=DNI, row[3]=Nombre...
                
                # Convertir fecha dd/mm/aaaa a objeto Date
                fecha_nac = None
                if row[4]:
                    try:
                        fecha_nac = datetime.strptime(row[4], '%d/%m/%Y').date()
                    except ValueError:
                        pass # Si la fecha está mal, la dejamos Null o manejamos error

                nuevo_alumno = Alumno(
                    facultad_id=int(row[0]),
                    tipo_documento=int(row[1]),
                    nro_documento=int(row[2]),
                    nombre_completo=row[3], 
                    fecha_nacimiento=fecha_nac,
                    sexo=row[5],
                    nro_legajo=int(row[6]) if row[6] else None
                )
                
                # Llamamos al guardar CON RETRY (Requisito Parcial 2)
                AlumnoService.guardar_con_retry(nuevo_alumno)
                procesados += 1
                
            except Exception as e:
                errores += 1
                print(f"Error en fila: {e}")

        return {"procesados": procesados, "errores": errores}

    @staticmethod
    @retry(max_attempts=3, delay=1.0) # <--- ¡ESTO ES VITAL!
    def guardar_con_retry(alumno):
        db.session.add(alumno)
        db.session.commit()