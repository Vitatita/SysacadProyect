import unittest
from flask import current_app
from app import create_app
import os
from app.models import universidad

class TestUniversidad(unittest.TestCase):

    def setUp(self):
        # Seteamos la configuración de testing
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_universidad_exists(self):
        self.assertFalse(current_app is None)

    def test_universidad_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
