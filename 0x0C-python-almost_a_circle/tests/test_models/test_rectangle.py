#!/usr/bin/python3
""" This script contains all egde cases to test the codes """
from models.rectangle import Rectangle
import models.rectangle
import unittest
import os


class TestBaseClass(unittest.TestCase):
    """ Class to test the class Rectangle with the module unittest """
    def test_shebang(self):
        with open('models/rectangle.py', 'r') as fd:
            text = fd.read()
            line = text.splitlines()
        self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_pep8(self):
        self.assertEqual(os.system('pep8 models/rectangle.py'), 0)

    def test_documentation(self):
        self.assertTrue(len(models.rectangle.__doc__) > 0)

    def test_doc_class(self):
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_doc_function_area(self):
        self.assertTrue(len(Rectangle.area.__doc__) > 0)

    def test_doc_function_display(self):
        self.assertTrue(len(Rectangle.display.__doc__) > 0)

    def test_doc_function_str(self):
        self.assertTrue(len(Rectangle.__str__.__doc__) > 0)

    def test_doc_function_update(self):
        self.assertTrue(len(Rectangle.update.__doc__) > 0)

    def test_doc_function_to_dictionary(self):
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 0)

    def test_exception_type(self):
        with self.assertRaises(TypeError):
            Rectangle('Holberton', 10)

    def test_exception_value(self):
        with self.assertRaises(ValueError):
            Rectangle(16, 22, -6, 4)

    def test_exception_type_error(self):
        with self.assertRaises(TypeError):
            a = Rectangle(100, 100)
            a.y = []

    def test_area_method(self):
        a = Rectangle(20, 30)
        self.assertEqual(a.area(), 600)

if __name__ == '__name__':
    unittest.main()
