#!/usr/bin/python3

""" A module containing a function, class_to_json """

import json


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

    if isinstance(obj, bool) or isinstance(obj, int) or isinstance(obj, str):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        return {key: class_to_json(value) for key,
                value in obj.__dict__.items()}
    else:
        return None
