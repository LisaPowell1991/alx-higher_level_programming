#!/usr/bin/python3

""" This module contains a function, is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class

    Args:
    @obj: The object to be inspected
    @a_class: The class to compare with

    Returns:
    True if the object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class; otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
