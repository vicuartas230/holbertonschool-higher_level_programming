#!/usr/bin/python3
""" This script contains all egde cases to test the codes """
from models.base import Base
import models.base
import unittest
import os

class TestBaseClass(unittest.TestCase):
    """ Class to test the class Base with the module unittest """
    def test_shebang(self):
        with open('models/base.py', 'r') as fd:
            text = fd.read()
            line = text.splitlines()
        self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_pep8(self):
        self.assertEqual(os.system('pep8 models/base.py'), 0)

    def test_documentation(self):
        self.assertTrue(len(models.base.__doc__) > 0)

    def test_doc_class(self):
        self.assertTrue(len(Base.__doc__) > 0)

    def test_doc_function_to_json_string(self):
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)
        
    def test_doc_function_save_to_file(self):
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)

    def test_doc_function_from_json_string(self):
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)

    def test_doc_function_create(self):
        self.assertTrue(len(Base.create.__doc__) > 0)

    def test_doc_function_load_from_file(self):
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    def test_to_json_string_None(self):
        a = Base.to_json_string(None)
        self.assertTrue(len(a) == 2)

    def test_to_json_string(self):
        dicts = []
        self.assertEqual(type(Base.to_json_string(dicts)), str)

if __name__ == '__name__':
    unittest.main()
