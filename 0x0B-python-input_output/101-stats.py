#!/usr/bin/python3
import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
file_size = 0
try:
    for i, line in enumerate(sys.stdin, 1):
        split_line = line.split()
        status_code = int(split_line[-2])
        file_size += int(split_line[-1])
        if status_code in status_codes:
            status_codes[status_code] += 1
        if i % 10 == 0:
            print("File size: {}".format(file_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
