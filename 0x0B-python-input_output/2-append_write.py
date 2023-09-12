#!/usr/bin/python3

""" A module containing a function, append_write """


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file
    and returns the number of characters added

    Args:
    @filename: Name of file to write
    @text: The content

    Returns:
    The number of characters addded
    """

    with open(filename, "a", encoding='utf-8') as myfile:
        appended_chars = myfile.write(text)
        return appended_chars
