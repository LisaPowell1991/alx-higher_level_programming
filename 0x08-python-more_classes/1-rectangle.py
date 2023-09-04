#!/usr/bin/python3

""" This module represents a class, Rectangle """


class Rectangle:
    """ This class defines a rectangle

    Attributes:
    __width (int): Width of rectangle
    __height (int): Height of rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Retangle instance with optional width and height.

        Args:
        width (int, optional): Width of rectangle(default is 0)
        height (int, optional): Height of rectangle(defult is 0)
        """

        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle

        Returns:
        int: the width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with error checking

        Args:
        value (int): The new width value

        Raises:
        TypeError: If value is not an int
        ValueError: If value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle

        Returns:
        int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of rectangle with error checking

        Args:
        value (int): The new height value

        Raises:
        TypeError: If value is not an int
        ValueError: If value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
