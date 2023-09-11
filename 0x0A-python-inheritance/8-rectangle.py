#!/usr/bin/python3

""" This module contains an empty class, BaseGeometry. """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Represent a Rectangle class that inherits from  BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
        @width (int): The width of the rectangle
        @height int: The height of the rectangle

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than or equal to 0.
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
