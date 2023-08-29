#!/usr/bin/python3

""" This module provides a class Square"""


class Square:
    """
    This class defines a square with a given size

    Attributes:
        ___size (int): The size of the square (private)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializing a new Square instance

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square (default is (0, 0))
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets or sets the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            int: The size of the square's sides.
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

    @property
    def position(self):
        """
        Get or set the position of the square.

        Raises:
        TypeError: If position is not a tuple of 2 positive integers

        Returns:
        tuple: The position of the square.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(v, int) for v in value) or
                not all(v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
