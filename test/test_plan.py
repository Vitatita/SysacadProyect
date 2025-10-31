import unittest
from flask import current_app
from app import create_app
import os
from app.models import Plan, Facultad
class PlanTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_plan_creation(self):
        plan = Plan()
        facultad = Facultad()

        
        plan.nombre = "Plan de Estudios en Matemáticas"
        plan.facultad = facultad

        facultad.nombre = "Facultad de Ciencias Exactas"
        
        self.assertIsNotNone(plan)
        self.assertEqual(plan.nombre, "Plan de Estudios en Matemáticas")
        self.assertIsNotNone(plan.facultad)
        self.assertEqual(plan.facultad.nombre, "Facultad de Ciencias Exactas")
