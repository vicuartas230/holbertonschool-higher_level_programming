#!/usr/bin/python3
""" This script contains all egde cases to test the codes """
from models.square import Square
import models.square
import unittest
import os
import sys
import io


class TestBaseClass(unittest.TestCase):
    """ Class to test the class Square with the module unittest """
    def test_shebang(self):
        with open('models/square.py', 'r') as fd:
            text = fd.read()
            line = text.splitlines()
        self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_pep8(self):
        self.assertEqual(os.system('pep8 models/square.py'), 0)

    def test_documentation(self):
        self.assertTrue(len(models.square.__doc__) > 0)

    def test_doc_class(self):
        self.assertTrue(len(Square.__doc__) > 0)

    def test_doc_function_update(self):
        self.assertTrue(len(Square.update.__doc__) > 0)

    def test_doc_function_to_dictionary(self):
        self.assertTrue(len(Square.to_dictionary.__doc__) > 0)

    def test_square(self):
        obj = Square(3, id=14)
        self.assertEqual(obj.__str__(), '[Square] (14) 0/0 - 3')
        comp = '###\n###\n###\n'
        output = io.StringIO()
        sys.stdout = output
        obj.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), comp)
        output.flush()

    def test_exception_type_error(self):
        with self.assertRaises(TypeError):
            obj = Square('Betty')

    def test_exception_value_error(self):
        with self.assertRaises(ValueError):
            obj = Square(-1)

    def test_square_update(self):
        obj = Square(2)
        self.assertEqual(obj.__str__(), '[Square] (3) 0/0 - 2')
        obj = Square(4)

    def test_square_to_dictionary(self):
        obj = Square(3, 7, 1, 1)
        self.assertEqual(obj.__str__(), '[Square] (1) 7/1 - 3')
        obj_dict = obj.to_dictionary()
        self.assertEqual(obj_dict.__str__(), "{'id': \
1, 'size': 3, 'x': 7, 'y': 1}")
        self.assertTrue(type(obj_dict) == dict)

        obj2 = Square(1, 1, 0, 1)
        self.assertEqual(obj2.__str__(), '[Square] (1) 1/0 - 1')
        obj2.update(**obj_dict)
        self.assertEqual(obj.__str__(), '[Square] (1) 7/1 - 3')

if __name__ == '__name__':
    unittest.main()
