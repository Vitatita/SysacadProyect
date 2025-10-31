import unittest
from flask import current_app
from app import create_app
import os
from app.models import Materia, Facultad
class MateriaTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_materia_creation(self):
        materia = Materia()
        facultad = Facultad()
        
        materia.nombre = "Matemáticas Avanzadas"
        materia.facultad = facultad

        
        facultad.nombre = "Facultad de Ciencias Exactas"

        
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, "Matemáticas Avanzadas")
        self.assertIsNotNone(materia.facultad)
        self.assertEqual(materia.facultad.nombre, "Facultad de Ciencias Exactas")
