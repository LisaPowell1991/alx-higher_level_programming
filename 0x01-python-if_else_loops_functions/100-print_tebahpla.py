#!/usr/bin/python3

letter_case = 0
for letter in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(letter - letter_case)), end="")
    letter_case = 32 - letter_case
