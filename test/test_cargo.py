import unittest
from flask import current_app
from app import create_app
import os
from app.models import Cargo,CategoriaCargo,TipoDedicacion

class CargoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_cargo_creation(self):
        cargo = Cargo()
        cargo.categoria_cargo = CategoriaCargo()
        cargo.tipo_dedicacion = TipoDedicacion()
        cargo.nombre = "Decano"
        cargo.puntos = 100
        cargo.categoria_cargo.nombre = "Categoria 1"
        cargo.tipo_dedicacion.nombre = "Dedicación 1"
        cargo.tipo_dedicacion.observacion = "Observación de prueba"
        self.assertIsNotNone(cargo)
        self.assertEqual(cargo.nombre, "Decano")
        self.assertEqual(cargo.puntos, 100)
        self.assertIsNotNone(cargo.categoria_cargo)
        self.assertEqual(cargo.categoria_cargo.nombre, "Categoria 1")
        self.assertIsNotNone(cargo.tipo_dedicacion)
        self.assertEqual(cargo.tipo_dedicacion.nombre, "Dedicación 1")
        self.assertEqual(cargo.tipo_dedicacion.observacion, "Observación de prueba")