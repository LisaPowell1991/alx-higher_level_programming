#!/usr/bin/python3

""" A module containing a function, class_to_json """


def class_to_json(obj):
    """
    A function that returns the dictionary
    description with simple data structure

    Args:
    @obj: Name of object

    Returns:
    The dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    value = {}

    if hasattr(obj, "__dict__"):
        value = obj.__dict__.copy()
    return value
