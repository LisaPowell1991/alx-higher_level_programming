#!/usr/bin/python3

"""
This module contains a function that adds
a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible

    Args:
    @obj: The object to which the attr should be added.
    @attr_name (str): The name of the attr
    @ttr_value: The value of the attr.

    Raises:
    TypeError: If the object can't have a new attr.
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
