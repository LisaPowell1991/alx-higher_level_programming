#!/usr/bin/python3

""" This module contains a subclass, Square that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represent a Square class that inherits from Rectangle. """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
        @size (int): the sides of the square
        """

        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ Calculates and returns the areaof the rectangle """

        return self.__size * self.__size

    def __str__(self):
        """ Return a string representation of the square """

        return (f"[Square] {self.__size}/{self.__size}")
