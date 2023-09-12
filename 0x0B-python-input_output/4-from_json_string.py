#!/usr/bin/python3

""" A module containing a function, from_json_string """

import json


def from_json_string(my_str):
    """
    A function that returns an object (string) represented by a JSON string

    Args:
    @my_str: Name of string that needs to be converted

    Returns:
    an object (Python data structure) represented by a JSON string
    """

    return (json.loads(my_str))
