#!/usr/bin/python3

""" A module that contains a class, Student """


class Student:
    """
    Represents a student with first name, last name and age attributes
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance

        Args:
        @first_name (str): The first name of the student
        @last_name (str): The last name of the student
        @age (int): The age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance

        Args:
        @attrs (list, optional): A list of attribute names to retrieve.
        Defaults to None.

        Returns:
        dict: A dictionary containing the selected student's attributes.
        """

        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
        @json: Is a dictionary containing attribute names and values.
        """

        for attr, value in json.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
