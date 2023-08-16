#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dictionary = {}

    multiply = lambda x: x * 2
    for key, value in a_dictionary.items():
        new_value = multiply(value)
        new_dictionary[key] = new_value

    return new_dictionary
