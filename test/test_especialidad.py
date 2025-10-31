import unittest
from flask import current_app
from app import create_app 
import os
from app.models import Especialidad, Facultad, TipoEspecialidad
class EspecialidadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_especialidad_creation(self):
        especialidad = Especialidad()
        facultad = Facultad()
        tipo_especialidad = TipoEspecialidad()
        
        especialidad.nombre = "Especialidad en Biología"
        especialidad.facultad = facultad
        especialidad.tipo_especialidad = tipo_especialidad
        
        facultad.nombre = "Facultad de Ciencias Naturales"
        tipo_especialidad.nombre = "Tipo B"
        
        self.assertIsNotNone(especialidad)
        self.assertEqual(especialidad.nombre, "Especialidad en Biología")
        self.assertIsNotNone(especialidad.facultad)
        self.assertEqual(especialidad.facultad.nombre, "Facultad de Ciencias Naturales")
        self.assertIsNotNone(especialidad.tipo_especialidad)
        self.assertEqual(especialidad.tipo_especialidad.nombre, "Tipo B")