#!/usr/bin/python3

""" This module defines unittest cases for Rectangle """

import unittest
import io
import sys
import json
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for the Rectangle class """

    def test_rectangle_exists(self):
        """
        Test if a Rectangle instance with dimensions (1, 2) exists.
        """
        rect = Rectangle(1, 2)
        self.assertIsInstance(rect, Rectangle)

    def test_rectangle_with_valid_values(self):
        """
        Test creating a Rectangle with valid
        width, height, x and y values.
        """

        rectangle = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_rectangle_with_negative_width(self):
        """
        Test creating a Rectangle with a negative width.
        (Should raise ValueError)
        """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-5, 20, 2, 3, 1)

    def test_rectangle_with_negative_height(self):
        """
        Test creating a Rectangle with a negative height.
        (Should raise ValueError)
        """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, -5, 2, 3, 1)

    def test_rectangle_with_negative_x(self):
        """
        Test creating a Rectangle with a negative x.
        (Should raise ValueError)
        """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 5, -2, 20, 5)

    def test_rectangle_with_negative_y(self):
        """
        Test creating a Rectangle with a negative y.
        (Should raise ValueError)
        """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 8, 4, -10, 1)

    def test_rectangle_with_non_integer_width(self):
        """
        Test creating a Rectangle with a non-integer width
        (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle("invalid_width", 9)

    def test_rectangle_with_non_integer_height(self):
        """
        Test creating a Rectangle with a non-integer height
        (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, "invalid", 5, 1, 3)

    def test_rectangle_with_non_integer_x(self):
        """
        Test creating a Rectangle with a non-integer x
        (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(13, 6, "invalid", 3, 1)

    def test_rectangle_with_non_integer_y(self):
        """
        Test creating a Rectangle with a non-integer y
        (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(14, 8, 20, "invalid", 1)

    def test_default_id_assigned(self):
        """
        Test that a Rectangle gets assigned
        a unique ID if none is provided.
        """

        rectangle1 = Rectangle(10, 20)
        rectangle2 = Rectangle(5, 8)
        self.assertNotEqual(rectangle1.id, rectangle2.id)


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_calculation(self):
        """
        Test that the area() method works correctly
        """
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_area_with_zero_width(self):
        """
        Test that area method correctly handles
        a rectangle with 0 width
        """
        with self.assertRaises(ValueError):
            # Creating a Rectangle instance with zero width
            rectangle = Rectangle(0, 10)

    def test_area_with_negative_width(self):
        """
        Test that area method correctly handles
        a rectangle with negative width
        """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-5, 10)
            area = rectangle.area()

    def test_area_with_large_values(self):
        """
        Test that the area() method handles
        very large width and height values.
        """
        rectangle = Rectangle(10**9, 10**9)
        self.assertEqual(rectangle.area(), 10**18)

    def test_area_with_non_integer_width(self):
        """
        Test that the area() method correctly
        handles a non-integer width.
        """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(10.5, 10)
            area = rectangle.area()


class TestRectangleDisplay(unittest.TestCase):
    """
    Test cases for the Rectangle class display, __str__ and update method
    """

    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_display_without_x_y(self):
        r = Rectangle(4, 3)
        r.display()
        expected_output = "####\n####\n####\n"
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_display_without_y(self):
        r = Rectangle(4, 3, 2)
        r.display()
        expected_output = "  ####\n  ####\n  ####\n"
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_display_with_x_and_y(self):
        r = Rectangle(4, 3, 2, 1)
        r.display()
        expected_output = "\n  ####\n  ####\n  ####\n"
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_str_reprensentation(self):
        """
        Test that the __str__() method
        returns the expected string format.
        """
        rectangle = Rectangle(7, 14, 2, 3, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 2/3 - 7/14")


class TestRectangleToDictionary(unittest.TestCase):

    def test_to_dictionary_exists(self):
        """
        Test if to_dictionary method exists in Rectangle class
        and returns the expected dictionary representation.
        """
        r = Rectangle(4, 3, 2, 1, 42)
        expected_dict = {
            "id": 42,
            "width": 4,
            "height": 3,
            "x": 2,
            "y": 1
        }
        self.assertEqual(r.to_dictionary(), expected_dict)


class TestRectangleUpdate(unittest.TestCase):
    """  Test cases for the Rectangle class """

    def test_update_with_args(self):
        """
        Test updating attributes of Rectangle using positional arguments.
        """
        r = Rectangle(4, 3)
        r.update(1, 2, 5, 6, 7)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)

    def test_update_with_kwargs(self):
        """
        Test updating attributes of Rectangle using keyword arguments.
        """
        r = Rectangle(4, 3)
        r.update(id=1, width=2, height=5, x=6, y=7)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)

    def test_update_with_mixed_args_and_kwargs(self):
        """
        Test updating attributes of Rectangle using a mix of args and kwargs.
        """
        r = Rectangle(4, 3)
        r.update(1, width=2, height=5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 5)


if __name__ == "__main__":
    unittest.main()
