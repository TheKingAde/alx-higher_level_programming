#!/usr/bin/python3
def print_tebahpla():
    alphabet = ""
    for i in range(122, 96, -1):
        if i % 2 == 0:
            alphabet += "{:s}".format(chr(i).lower())
        else:
            alphabet += "{:s}".format(chr(i).upper())
    print("{:s}".format(alphabet), end="")


print_tebahpla()
