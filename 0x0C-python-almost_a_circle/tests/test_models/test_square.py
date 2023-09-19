#!/usr/bin/python3

""" This module defines unittest cases for Square """

import unittest
import io
import sys
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test cases for the Rectangle class """

    def test_square_with_size(self):
        """
        Test creating a Square with only size
        """

        square = Square(5)
        self.assertEqual(square.size, 5)
