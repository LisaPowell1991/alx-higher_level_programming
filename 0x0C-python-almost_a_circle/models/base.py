#!/usr/bin/python3

""" This module contains a class Base """


class Base:
    """
    Base class for managing ID attributes in other classes.

    Attributes:
    __nb_objects (int): A private class attribute to
    keep track of num of objects created.
    id (int): A public instance attribute
    representing the unique ID of an object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object

        Args:
        id (int, optional): An optional int ID for the object.
        If not provided, a unique ID will be generated.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1

            self.id = Base.__nb_objects
