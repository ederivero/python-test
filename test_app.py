from app import app
import unittest
from unittest import TestCase


class TestFlask(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def testTareas(self):
        data = self.app.get('/tareas')
        self.assertEqual(data.json, {'message': 'las tareas son:'})


if __name__ == '__main__':
    unittest.main()
