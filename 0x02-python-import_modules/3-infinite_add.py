#!/usr/bin/python3

import sys

def add_args():
    total = 0

    for argument in sys.argv[1:]:
        total += int(argument)

    print("{}".format(total))

if __name__ == "__main__":
    add_args()
