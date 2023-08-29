#!/usr/bin/python3

""" This module provides a class Square"""


class Square:
    """
    This class defines a square with a given size

    Attributes:
    __size (int): The size of the square (private)
    """

    def __init__(self, size):
        """
        Initializing a Square instance

        Args:
        size (int): The size of the square.
        """

        self.__size = size
