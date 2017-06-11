#!/usr/bin/env python3
"""Test the db_department library in the infoset.db module."""

import unittest
import os
import sys

# Try to create a working PYTHONPATH
_TEST_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
_LIB_DIRECTORY = os.path.abspath(os.path.join(_TEST_DIRECTORY, os.pardir))
_ROOT_DIRECTORY = os.path.abspath(os.path.join(_LIB_DIRECTORY, os.pardir))
if _TEST_DIRECTORY.endswith('/infoset/test') is True:
    sys.path.append(_ROOT_DIRECTORY)
else:
    print(
        'This script is not installed in the "infoset-ng/bin" directory. '
        'Please fix.')
    sys.exit(2)

from infoset.db import db_department
from infoset.test import unittest_setup_db
from infoset.test import unittest_setup


class TestGetIDXDepartment(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    # Setup database based on the config
    database = unittest_setup_db.TestData()

    # Define expected values
    expected = {}
    expected['idx_department'] = database.idx_department()
    expected['name'] = database.department_name()
    expected['code'] = database.department_code()
    expected['enabled'] = True
    expected['exists'] = True

    # Retrieve data
    good_agent = db_department.GetIDXDepartment(expected['idx_department'])

    def test_init_(self):
        """Testing method init."""
        # Test with non existent AgentIDX
        record = db_department.GetIDXDepartment(-1)
        self.assertEqual(record.exists(), False)

    def test_idx_department(self):
        """Testing method idx_department."""
        # Testing with known good value
        result = self.good_agent.idx_department()
        self.assertEqual(result, self.expected['idx_department'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.idx_department()
        self.assertNotEqual(result, expected)

    def test_name(self):
        """Testing method name."""
        # Testing with known good value
        result = self.good_agent.name()
        self.assertEqual(result, self.expected['name'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.name()
        self.assertNotEqual(result, expected)

    def test_code(self):
        """Testing method code."""
        # Testing with known good value
        result = self.good_agent.code()
        self.assertEqual(result, self.expected['code'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.code()
        self.assertNotEqual(result, expected)

    def test_exists(self):
        """Testing method exists."""
        # Testing with known good value
        result = self.good_agent.exists()
        self.assertEqual(result, True)

    def test_enabled(self):
        """Testing method enabled."""
        # Testing with known good value
        result = self.good_agent.enabled()
        self.assertEqual(result, self.expected['enabled'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.enabled()
        self.assertNotEqual(result, expected)

    def test_everything(self):
        """Testing method everything."""
        # Testing with known good value
        result = self.good_agent.everything()
        for key, _ in self.expected.items():
            self.assertEqual(result[key], self.expected[key])

        # Test the number and names of keys
        keys = ['idx_department', 'code', 'name', 'enabled', 'exists']
        self.assertEqual(len(result), len(keys))
        for key in keys:
            self.assertEqual(key in result, True)


class TestGetCodeDepartment(unittest.TestCase):
    """Checks all functions and methods."""

    # Setup database based on the config
    database = unittest_setup_db.TestData()

    # Define expected values
    expected = {}
    expected['idx_department'] = database.idx_department()
    expected['name'] = database.department_name()
    expected['code'] = database.department_code()
    expected['enabled'] = True
    expected['exists'] = True

    # Retrieve data
    good_agent = db_department.GetCodeDepartment(expected['code'])

    def test_init_getcode(self):
        """Testing method __init__."""
        # Test with non existent AgentID
        record = db_department.GetCodeDepartment('bogus')
        self.assertEqual(record.exists(), False)

    def test_idx_department(self):
        """Testing method idx_department."""
        # Testing with known good value
        result = self.good_agent.idx_department()
        self.assertEqual(result, self.expected['idx_department'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.idx_department()
        self.assertNotEqual(result, expected)

    def test_name(self):
        """Testing method name."""
        # Testing with known good value
        result = self.good_agent.name()
        self.assertEqual(result, self.expected['name'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.name()
        self.assertNotEqual(result, expected)

    def test_code(self):
        """Testing method code."""
        # Testing with known good value
        result = self.good_agent.code()
        self.assertEqual(result, self.expected['code'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.code()
        self.assertNotEqual(result, expected)

    def test_exists(self):
        """Testing method exists."""
        # Testing with known good value
        result = self.good_agent.exists()
        self.assertEqual(result, True)

    def test_enabled(self):
        """Testing method enabled."""
        # Testing with known good value
        result = self.good_agent.enabled()
        self.assertEqual(result, self.expected['enabled'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.enabled()
        self.assertNotEqual(result, expected)

    def test_everything(self):
        """Testing method everything."""
        # Testing with known good value
        result = self.good_agent.everything()
        for key, _ in self.expected.items():
            self.assertEqual(result[key], self.expected[key])

        # Test the number and names of keys
        keys = ['idx_department', 'code', 'name', 'enabled', 'exists']
        self.assertEqual(len(result), len(keys))
        for key in keys:
            self.assertEqual(key in result, True)


class TestFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    # Setup database based on the config
    database = unittest_setup_db.TestData()

    # Define expected values
    expected = {}
    expected['idx_department'] = database.idx_department()
    expected['name'] = database.department_name()
    expected['code'] = database.department_code()
    expected['enabled'] = True
    expected['exists'] = True

    def test_code_exists(self):
        """Testing function code_exists."""
        # Testing with known good value
        expected = True
        result = db_department.code_exists(self.expected['code'])
        self.assertEqual(result, expected)

        # Testing with known bad value
        expected = False
        result = db_department.code_exists('bogus')
        self.assertEqual(result, expected)

    def test_idx_department_exists(self):
        """Testing function idx_department_exists."""
        # Testing with known good value
        expected = True
        result = db_department.idx_department_exists(
            self.expected['idx_department'])
        self.assertEqual(result, expected)

        # Testing with known bad value
        expected = False
        result = db_department.idx_department_exists(None)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Test the environment variables
    unittest_setup.ready()

    # Do the unit test
    unittest.main()
