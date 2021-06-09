#!/usr/bin/python3
""" This script contains all egde cases to test the codes """
from models.rectangle import Rectangle
import models.rectangle
import unittest
import os
import io
import sys


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
        with self.assertRaises(TypeError):
            Rectangle(5, 'V')
        with self.assertRaises(TypeError):
            Rectangle(20, 10, [6, 7, 8])
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 10, (5, 6, 7))

    def test_exception_value(self):
        with self.assertRaises(ValueError):
            Rectangle(16, 22, -6, 4)
        with self.assertRaises(ValueError):
            Rectangle(5, 0)
        with self.assertRaises(ValueError):
            Rectangle(-7, 2)
        with self.assertRaises(ValueError):
            Rectangle(135, 6984, 541, -64)

    def test_exception_type_error(self):
        with self.assertRaises(TypeError):
            a = Rectangle(100, 100)
            a.y = []

    def test_area_method(self):
        a = Rectangle(20, 30)
        self.assertEqual(a.area(), 600)

    def test_str_method(self):
        obj = Rectangle(5, 6, 0, 0, 78)
        self.assertEqual(obj.__str__(), "[Rectangle] (78) 0/0 - 5/6")

    def test_display_0(self):
        obj = Rectangle(2, 3)
        comp = '##\n##\n##\n'
        output = io.StringIO()
        sys.stdout = output
        obj.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), comp)
        output.flush()

    def test_display_1(self):
        obj = Rectangle(2, 3, 2, 1)
        comp = '\n  ##\n  ##\n  ##\n'
        output = io.StringIO()
        sys.stdout = output
        obj.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), comp)
        output.flush()

    def test_update_0(self):
        obj = Rectangle(1, 1, 1, 1)
        obj.update(85)
        self.assertEqual(obj.id, 85)
        obj.update(85, 6)
        self.assertEqual(obj.width, 6)

    def test_update_1(self):
        obj = Rectangle(1, 1, 1, 1, 1)
        obj.update(height=45)
        self.assertEqual(obj.__str__(), '[Rectangle] (1) 1/1 - 1/45')
        obj.update(width=64, x=3)
        self.assertEqual(obj.__str__(), '[Rectangle] (1) 3/1 - 64/45')
        obj.update(y=0, width=4, x=21, id=6541)
        self.assertEqual(obj.__str__(), '[Rectangle] (6541) 21/0 - 4/45')

if __name__ == '__name__':
    unittest.main()
