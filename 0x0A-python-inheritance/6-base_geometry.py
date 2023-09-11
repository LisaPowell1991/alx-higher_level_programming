#!/usr/bin/python3

""" This module contains an empty class, BaseGeometry. """


class BaseGeometry:
    """
    This class defines BaseGeometry class
    """

    def area(self):
        """
        A public instance method, called area, that calculates the area

        Raises:
        Exception is raised if subclass does not implement this method
        """

        raise Exception("area() is not implemented")
