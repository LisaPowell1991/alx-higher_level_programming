#!/usr/bin/python3

""" This module defines a class, Square. """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represents a square that inherits from rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
        size (int): The size of the square
        x (int, optional): The x-coordinate of the square.
        y (int, optional): The y-coordinate of the square.
        id (int, optional): Id of the square
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Custom string representation of the Square. """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Get the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square (both width and height).

        Args:
        value (int): The new size of the square.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assign arguments or key-value pairs to attributes.

        Args:
        *args: List of arguments (no-keyworded)
        in the order id, size, x, y.
        **kwargs: Dictionary of keyworded arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
