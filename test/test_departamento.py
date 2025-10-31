import unittest
from flask import current_app
from app import create_app
import os
from app.models import Departamento, Facultad
class DepartamentoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_departamento_creation(self):
        departamento = Departamento()
        facultad = Facultad()
        
        departamento.nombre = "Departamento de Ciencias"
        departamento.facultad = facultad

        
        facultad.nombre = "Facultad de Ciencias Exactas"
        
        self.assertIsNotNone(departamento)
        self.assertEqual(departamento.nombre, "Departamento de Ciencias")
        self.assertIsNotNone(departamento.facultad)
        self.assertEqual(departamento.facultad.nombre, "Facultad de Ciencias Exactas")
