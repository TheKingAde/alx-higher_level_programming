#!/usr/bin/python3

import sys


def main():
    args = sys.argv
    num_args = len(args) - 1

    if num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    main()
