#!/usr/bin/python3

""" A module containing a function, save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation.

    Args:
    @my_obj: Name of the object to be saved
    @filename: Name of file where you want to save the JSON obj
    """

    with open(filename, "w") as myfile:
        json.dump(my_obj, myfile)
