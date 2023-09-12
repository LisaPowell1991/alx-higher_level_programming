#!/usr/bin/python3

""" A module containing a function, read_file """


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding='utf-8') as myfile:
        content = myfile.read()
        print(content, end="")
