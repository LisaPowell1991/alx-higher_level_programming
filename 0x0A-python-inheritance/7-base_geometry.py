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

    def integer_validator(self, name, value):
        """
        A public instance method, called integer_validator that validates value

        Args:
        @name: The name of the value
        @value: The value to be validated

        Raises:
        TypeError: If value is not an integer
        ValueError: if value is <= 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
