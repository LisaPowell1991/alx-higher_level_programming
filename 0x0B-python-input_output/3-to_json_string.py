#!/usr/bin/python3

""" A module containing a function, to_json_string """

import json

def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object (string)

    Args:
    @my_obj: Name of object

    Returns:
    returns the JSON representation of an object (string)
    """

    return (json.dumps(my_obj))
