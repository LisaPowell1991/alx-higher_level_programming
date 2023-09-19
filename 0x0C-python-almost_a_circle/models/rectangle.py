#!/usr/bin/python3

""" This module contains a class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ A class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object

        Args:
        width (int): Width of rectangle
        height (int): Height of rectangle
        x (int, optional): The x-coordinate of the new Rectangle.
        y (int, optional): The y-coordinate of the new Rectangle.
        id (int, optional): Id of the new Rectangle

        """

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Sets the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Sets the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ Sets the x coordinates of the Rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Sets the y coordinates of the Rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Determines the area value of the Rectangle """
        return self.width * self.height

    def display(self):
        """
        Display the Rectangle instance with '#' characters,
        accounting for x and y.
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
