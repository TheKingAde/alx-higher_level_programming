#!/usr/bin/python3
import random
number = random.randint(-10, 10)


def check_number(number):
    if number > 0:
        print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")


check_number(number)
