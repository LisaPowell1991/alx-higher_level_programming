#!/usr/bin/python3

""" This module defines unittest cases for Rectangle """

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for the Rectangle class """

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
            rectangle = Rectangle("invalid", 20, 3, 7, 9)

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


if __name__ == "__main__":
    unittest.main()