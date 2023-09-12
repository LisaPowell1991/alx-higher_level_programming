#!/usr/bin/python3

""" A module containing a function, write_file """


def write_file(filename="", text=""):
    """
    a function thatwrites a string to a text file (UTF8)
    and the number of characters written

    Args:
    @filename: Name of file to write
    @text: The content

    Returns:
    The number of characters written
    """

    with open(filename, "w", encoding='utf-8') as myfile:
        char_count = myfile.write(text)
        return char_count
