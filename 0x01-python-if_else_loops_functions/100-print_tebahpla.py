#!/usr/bin/python3
def print_tebahpla():
    alphabet = ""
    for i in range(122, 96, -1):
        if i % 2 == 0:
            alphabet += chr(i).lower()
        else:
            alphabet += chr(i).upper()
    print(alphabet, end="")


print_tebahpla()
