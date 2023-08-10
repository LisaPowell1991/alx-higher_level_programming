#!/usr/bin/python3

import sys

def print_args():
    num_args =  len(sys.argv) - 1

    if num_args == 0:
        print("0 arguments.")
        return

    args_plural = "argument" if num_args == 1 else "arguments"
    print("{} {}:".format(num_args, args_plural))

    for i in range(1, num_args + 1):
        arg = sys.argv[i]
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_args()

