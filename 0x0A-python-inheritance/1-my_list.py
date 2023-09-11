#!/usr/bin/python3

""" This module contains a class, MyList """


class MyList(list):
    """
    A custom class, MyList that inherits from list.
    It contains a Public instance method, print_sorted.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)

        Returns:
        None
        """
        sorted_list = sorted(self)

        print(sorted_list)
