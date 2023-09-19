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
        id (int, optional): Id of the new Rectangle.

        Raises:
        TypeError: If width, height, x, or y is not an integer.
        ValueError: If width or height is less than or equal to 0,
        or if x or y is less than 0.

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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Sets the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

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

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute in order:
        id, width, height, x, y

        Args:
        *args: A tuple of arguments containing values
        for id, width, height, x, and y.
        *kwargs: a double pointer to a dictionary: key/value
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation
        of the Rectangle

        Returns:
        dict: A dictionary containing
        id, width, height, x, and y.
        """

        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }
