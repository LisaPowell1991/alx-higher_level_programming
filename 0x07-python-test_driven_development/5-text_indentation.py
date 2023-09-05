#!/usr/bin/python3

""" A module that contains a class, text_indentation """


def text_indentation(text):
    """
    prints a text with 2 new lines after each
    of these characters: ., ? and :

    Args:
    text: The input text to be formatted.

    Raises:
    TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise("text must be a string")

    current_line = ""

    for char in text:
        current_line += char
        if char in ('.', '?', ':'):
            print(current_line.strip())
            print()
            current_line = ""

    # Print the last line if it's not empty
    if current_line:
        print(current_line.strip(), end="")
