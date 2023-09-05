#!/usr/bin/python3

""" Module that contains a class add_integer """


def add_integer(a, b=98):
    """
    This class adds two integers or floats
    and returns ressult as  an int

    Args:
    param a: The first int or float
    param b: the second int or float (default is 98)

    Raises:
    TyperError: If a or b is not an int or float

    Returns:
    The int result of adding a and b
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
