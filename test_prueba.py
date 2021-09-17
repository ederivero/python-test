from unittest import TestCase
import unittest


class PruebasTest(TestCase):
    def setUp(self):
        self.number = 10

    def test_number(self):
        self.assertEqual(self.number, 10)


if __name__ == '__main__':
    unittest.main()
