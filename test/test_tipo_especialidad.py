import unittest
from flask import current_app
from app import create_app
import os
from app.models import TipoEspecialidad, Facultad, Especialidad
class TipoEspecialidadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_tipo_especialidad_creation(self):
        tipo_especialidad = TipoEspecialidad()
        facultad = Facultad()
        especialidad = Especialidad()
        
        tipo_especialidad.nombre = "Tipo B"
        facultad.nombre = "Facultad de Ciencias Naturales"
        especialidad.nombre = "Especialidad en Biología"
        
        tipo_especialidad.facultad = facultad
        especialidad.tipo_especialidad = tipo_especialidad
        
        self.assertIsNotNone(tipo_especialidad)
        self.assertEqual(tipo_especialidad.nombre, "Tipo B")
        self.assertIsNotNone(tipo_especialidad.facultad)
        self.assertEqual(tipo_especialidad.facultad.nombre, "Facultad de Ciencias Naturales")
        self.assertIsNotNone(especialidad)
        self.assertEqual(especialidad.nombre, "Especialidad en Biología")
        self.assertIsNotNone(especialidad.tipo_especialidad)
        self.assertEqual(especialidad.tipo_especialidad.nombre, "Tipo B")   