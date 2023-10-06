#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]
    total = 0

    for arg in args:
        try:
            total += int(arg)
        except ValueError:
            print(f"Warning: '{arg}' is not a number and was skipped.")
    print(total)


if __name__ == "__main__":
    main()
