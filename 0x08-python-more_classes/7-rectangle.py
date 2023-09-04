#!/usr/bin/python3

""" This module represents a class, Rectangle """


class Rectangle:
    """ This class defines a rectangle

    Attributes:
    __width (int): Width of rectangle
    __height (int): Height of rectangle
    """

    print_symbol = '#'
    number_of_instances = 0

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

        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculate and return the area of the rectangle

        Returns:
        int: The area of the rectangle.
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle

        Returns:
        int: The perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Customize the string representation of the rectangle

        Returns:
        str: The string representation of the rectangle with '#'
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(Rectangle.print_symbol) * self.__width + "\n"

        return rectangle_str.rstrip()

    def __repr__(self):
        """
        Customize the representation of the rectangle for eval()

        Returns:
        str: The string representation of the rectangle that can
        recreate a new instance
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message when an instance of Rectangle is deleted """

        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
