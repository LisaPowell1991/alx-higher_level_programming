#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as value_error_exception:
        print("Exception:", value_error_exception, file=sys.stderr)
        return False
