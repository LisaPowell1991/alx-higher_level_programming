#!/usr/bin/python3

""" Module that contains a class, say_my_name """


def say_my_name(first_name, last_name=""):
    """
    a function that prints My name is <first name> <last name>

    Args:
    first_name: String that represents first name of a person
    last_name: String that represents last name of a person

    Raises:
    TypeError: If either the first_name or last_name is not a string

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
