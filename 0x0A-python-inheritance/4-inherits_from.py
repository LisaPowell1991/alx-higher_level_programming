#!/usr/bin/python3

""" This module contains a function, inherits_from """


def inherits_from(obj, a_class):
    """
    checks if  object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Args:
    @obj: The object to be inspected
    @a_class: The class to compare with

    Returns:
    Bool: True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
