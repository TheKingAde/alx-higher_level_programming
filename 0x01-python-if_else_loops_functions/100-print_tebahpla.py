#!/usr/bin/python3
for char in range(ord('z'), ord('A') - 1, -1):
    if char < ord('a') and char > ord('Z'):
        continue
    print("{:c}".format(char if char % 2 == 0 else char - 32), end="")
