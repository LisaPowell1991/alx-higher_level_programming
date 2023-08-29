#!/usr/bin/python3

""" This module provides a class Square"""


class Square:
    """
    This class defines a square with a given size

    Attributes:
        ___size (int): The size of the square (private)
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

        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size for the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square's area.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints in the square using thr '#' char.
        If size is 0, prints an empty line
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
