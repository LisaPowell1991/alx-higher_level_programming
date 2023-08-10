#!/usr/bin/python3

a = 10
b = 5

from calculator_1 import add, sub, mul, div
sum_total = add(a, b)
subtract_total = sub(a, b)
multiply_total = mul(a, b)
division_total = div(a, b)

print("{} + {} = {}".format(a, b, sum_total))
print("{} - {} = {}".format(a, b, subtract_total))
print("{} x {} = {}".format(a, b, multiply_total))
print("{} / {} = {}".format(a, b, division_total))
