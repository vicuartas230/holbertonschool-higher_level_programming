#!/usr/bin/python3
""" This script contains all egde cases to test the codes """
from models.square import Square
import models.square
import unittest
import os

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

if __name__ == '__name__':
    unittest.main()
