#!/usr/bin/python3

""" A module that contains a function, append after """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string

    Args:
    @filename (str): The file that is being modified.
    @search_string (str): The specific string to search for.
    @new_string (str): The line of text to insert after each line
    containing the search string.
    """

    if filename == "" or search_string == "":
        return

    with open(filename, 'r', encoding="utf-8") as myfile:
        lines = myfile.readlines()

    with open(filename, 'w', encoding="utf-8") as myfile:
        for line in lines:
            myfile.write(line)
            if search_string in line:
                myfile.write(new_string)
