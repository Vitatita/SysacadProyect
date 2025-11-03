import os
from docxtpl import DocxTemplate
from datetime import date
from docx2pdf import convert 


class CertificadoService:
    @staticmethod
    def generar_certificado(alumno, especialidad, facultad, universidad):
        plantilla_path = os.path.join("app","templates","certificado_plantilla.docx")
        doc = DocxTemplate(plantilla_path)

        context = {
            "alumno": alumno,
            "especialidad": especialidad,
            "facultad": facultad,
            "universidad": universidad,
            "fecha": date.today().strftime("%d de %B de %Y")
        }

        doc.render(context)
        
        # Nombre del archivo
        nombre_archivo = f"{alumno['nombre']}_{especialidad['nombre'].replace(' ', '_')}.docx"
        output_docx = os.path.join("app", "static", "certificados", nombre_archivo)

        # Crear carpeta si no existe
        os.makedirs(os.path.dirname(output_docx), exist_ok=True)
        
        #Guardar primero en DOCX
        doc.save(output_docx)

        # Convertir a PDF
        output_pdf = output_docx.replace(".docx", ".pdf")
        convert(output_docx, output_pdf)
        return output_pdf
