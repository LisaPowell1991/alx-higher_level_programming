#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ A test class for the max_integer function """

    def test_empty_list(self):
        """
        Test when an empty list is provided

        Returns:
        None
        """

        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_integers(self):
        """
        Test when a list with positive integers is provided

        Returns:
        The maximum int in the list
        """

        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_integers(self):
        """
        Test when a list with negative integers is provided

        Returns:
        The maximum int in the list
        """

        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_integers(self):
        """
        Test when a list with mixed positive and
        negative integers is provided

        Returns:
        The maximum int in the list
        """

        result = max_integer([-5, 0, 5, -10, 10])
        self.assertEqual(result, 10)

    def test_single_element_list(self):
        """
        Test when a list with a single element is provided

        Returns:
        The single element as the maximum
        """

        result = max_integer([42])
        self.assertEqual(result, 42)

if __name__ == "__main__":
    unittest.main()
