#!/usr/bin/python3

""" This module defines unittest cases for Base """

import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test class for the base class
    """

    def test_create_instance_with_id(self):
        """ Test creating instance  with a provided ID """
        instance = Base(42)
        self.assertEqual(instance.id, 42)

    def test_create_instance_with_negative_id(self):
        """ Test creating an instance with a negative ID. """
        instance = Base(-10)
        self.assertEqual(instance.id, -10)

    def test_create_instance_with_zero_id(self):
        """ Test creating an instance with an ID of zero. """
        instance = Base(0)
        self.assertEqual(instance.id, 0)

    def test_create_instance_without_id(self):
        """ Test creating an instance without providing an ID """
        instance1 = Base()
        self.assertEqual(instance1.id, 1)

    def test_to_json_string_with_none(self):
        """ Test if to_json_string(None) returns "[]". """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_empty_list(self):
        """ Test if to_json_string([]) returns "[]" """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_exists(self):
        """ Test if the to_json_string function exists """
        self.assertTrue(hasattr(Base, 'to_json_string'))

    def test_to_json_string_output(self):
        """ Test the output of the to_json_string function """
        input_data = [{'id': 12}]
        expected_output = json.dumps(input_data)

        self.assertEqual(Base.to_json_string(input_data), expected_output)


if __name__ == "__main__":
    unittest.main()
