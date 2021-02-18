#!/usr/bin/env python
"""
Unit tests for Valid Brackets.

Students should not modify this file.
"""

__author__ = 'pydan'

import sys
import unittest
import importlib
import subprocess

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True

# Kenzie devs: change this to 'soln.brackets' to test solution
PKG_NAME = 'brackets'


class TestValidBrackets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime."""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # this will import the module to be tested
        cls.module = importlib.import_module(PKG_NAME)

    def setUp(self):
        # assign the student's function to this instance
        self.is_valid = self.module.is_valid

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance."""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)

    def test_author_string(self):
        """Checking for author string."""
        self.assertIsNotNone(self.module.__author__)
        self.assertNotEqual(
            self.module.__author__, "???",
            "Author string is not completed"
        )

    def test_valid(self):
        """
        Check for a valid expression containing only bracket
        characters.
        """
        expr = "()"
        self.assertEqual(self.is_valid(expr), "YES")

    def test_valid_no_brackets(self):
        """
        Check for a valid expression containing no brackets.
        """
        expr = "*a*"
        self.assertEqual(self.is_valid(expr), "YES")

    def test_valid_chars(self):
        """
        Check for a valid expression containing brackets and
        non-bracket characters.
        """
        expr = "(a++)"
        self.assertEqual(self.is_valid(expr), "YES")

    def test_valid_multi(self):
        """
        Check for a valid expression containing multiple types
        of bracket characters.
        """
        expr = "(a{+})"
        self.assertEqual(self.is_valid(expr), "YES")

    def test_invalid_spaces(self):
        """Check for an invalid expression containing spaces."""
        expr = "  (a"
        self.assertEqual(self.is_valid(expr), "NO 5")

    def test_invalid_missing(self):
        """
        Check for an invalid expression that is missing a
        closing bracket.
        """
        expr = "(a++()"
        self.assertEqual(self.is_valid(expr), "NO 7")

    def test_invalid_mismatch(self):
        """
        Check for an invalid expression that contains a
        mismatched closing bracket.
        """
        expr = "([))"
        self.assertEqual(self.is_valid(expr), "NO 3")

    def test_invalid_long(self):
        """
        Check for a longer invalid expression that's more
        difficult to visually inspect.
        """
        expr = "({{}{}}[{(){}[]}"
        self.assertEqual(self.is_valid(expr), "NO 17")


if __name__ == '__main__':
    unittest.main()
