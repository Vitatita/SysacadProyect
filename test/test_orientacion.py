import unittest
from flask import current_app
from app import create_app
import os
from app.models.orientacion import Orientacion
from app.models.facultad import Facultad
class OrientacionTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    def test_orientacion_creation(self):
        orientacion = Orientacion()
        facultad = Facultad()
        
        orientacion.nombre = "Orientación en Matemáticas"
        orientacion.facultad = facultad
        
        facultad.nombre = "Facultad de Ciencias Exactas"
        
        self.assertIsNotNone(orientacion)
        self.assertEqual(orientacion.nombre, "Orientación en Matemáticas")
        self.assertIsNotNone(orientacion.facultad)
        self.assertEqual(orientacion.facultad.nombre, "Facultad de Ciencias Exactas")
        self.assertEqual(orientacion.facultad.nombre, "Facultad de Ciencias Exactas")
