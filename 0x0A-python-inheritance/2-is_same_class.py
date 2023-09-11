#!/usr/bin/python3

""" The module contains a fuction, is_same_class """


def is_same_class(obj, a_class):
    """
    Check if a object is exactly an instance of the specified class

    Args:
    @obj: The object to be inspected
    @a_class: The class to compare with

    Returns:
    bool: True if the object is exactly an instance of the specified class
    otherwise False.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
