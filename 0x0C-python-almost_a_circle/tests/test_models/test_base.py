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

    def test_doc_functions(self):
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)
        self.assertTrue(len(Base.create.__doc__) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

if __name__ == '__name__':
    unittest.main()
