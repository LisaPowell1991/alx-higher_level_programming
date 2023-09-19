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

        return f"[Squae] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Get the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square (both width and height).
        """
        self.width = value
        self.height = value
