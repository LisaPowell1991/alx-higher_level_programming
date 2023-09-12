#!/usr/bin/python3

""" A module containing a function, load_from_json_file """

import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”.

    Args:
    @filename: The name of the JSON file to load from.

    Returns:
    object: The object loaded from the JSON file,
    or None if the file is empty or doesn't contain valid JSON.
    """

    with open(filename, "r") as myfile:
        return (json.load(myfile))
