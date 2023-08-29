#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as value_error_exception:
        print("Exception:", value_error_exception, file=sys.stderr)
        return None
