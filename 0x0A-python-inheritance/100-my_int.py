#!/usr/bin/python3

""" This module contains a class, MyInt """


class MyInt(int):
    """ a class MyInt that inherits from int """

    def __eq__(self, value):
        """ Overrides the == operator to invert its behavior """

        return not super().__eq__(value)

    def __ne__(self, value):
        """ overrides the != operator to invert its behavior """

        return not super().__ne__(value)
