#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0

    for index in range(1, 3):
        try:
            if index > a:
                raise Exception('Too far')
        except ValueError:
            pass
        result = result + (a ** b) / index
    result = result + a + b
    return result
