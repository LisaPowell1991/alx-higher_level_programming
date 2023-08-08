#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = -(-number % 10)
else:
    last_digit = number % 10

msg = f"Last digit of {number:d} is {last_digit:d} and is"

if last_digit > 5:
    print(f"{msg} greater than 5")
elif last_digit == 0:
    print(f"{msg} 0")
elif last_digit < 6 and last_digit != 0:
    print(f"{msg} less than 6 and not 0")
