#!/usr/bin/python3

""" This module contains a functions, lookup """

def lookup(obj):
    """
    a function that returns the list of
    available attributes and methods of an object

    Args:
    @obj: The object that needs to be inspected

    Return:
    A list object
    """

    attributes_and_methods = dir(obj)

    return attributes_and_methods
