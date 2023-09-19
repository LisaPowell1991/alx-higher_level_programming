#!/usr/bin/python3

""" This module contains a class Base """

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serialize a list of dictionary into a JSON string

        Args:
        list_dictionaries (list of dict):
        The list of dictionaries to be serialized.

        Returns:
        str: The JSON string containing the list of dictionaries;
        If the input list is None or empty, returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
        list_objs (list): List of instances (objects) to be saved.

        Notes:
        The filename will be <Class name>.json (e.g. Square.json).
        If list_objs is None, an empty list will be saved to the file.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
            file.write(json_string)
