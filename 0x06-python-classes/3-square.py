#!/usr/bin/python3

""" This module provides a class Square"""


class Square:
    """
    This class defines a square with a given size

    Attributes:
    __size (int): The size of the square (private)
    """

    def __init__(self, size=0):
        """
        Initializing a Square instance with an optional size

        Args:
        size (int, optional): The size of the square. Defaults to 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the current square's area

        Returns:
        int: The area of the square.
        """

        return self.__size ** 2
