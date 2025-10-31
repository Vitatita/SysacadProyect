import unittest
from flask import current_app
from app import create_app
import os
from app.models import Autoridad,Cargo,CategoriaCargo,TipoDedicacion

class AutoridadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_autoridad_creation(self):
        autoridad = Autoridad()
        cargo = Cargo()
        cargo.categoria_cargo = CategoriaCargo()
        tipo_dedicacion = TipoDedicacion()
        autoridad.nombre = "Juan Pérez"
        autoridad.cargo = cargo   
        autoridad.telefono = "123456789"
        autoridad.email = "test@gmail.com"
        cargo.nombre = "Decano"
        cargo.puntos = 100
        cargo.categoria_cargo.nombre = "Categoria 1"
        tipo_dedicacion.nombre = "Dedicación 1"
        tipo_dedicacion.observacion = "Observación de prueba"
        self.assertIsNotNone(autoridad)
        self.assertEqual(autoridad.nombre, "Juan Pérez")
        self.assertIsNotNone(autoridad.cargo)
        self.assertEqual(autoridad.cargo.nombre, "Decano")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "test@gmail.com")
        self.assertIsNotNone(autoridad.cargo.categoria_cargo)
        self.assertEqual(autoridad.cargo.categoria_cargo.nombre, "Categoria 1")
        self.assertEqual(tipo_dedicacion.observacion, "Observación de prueba")