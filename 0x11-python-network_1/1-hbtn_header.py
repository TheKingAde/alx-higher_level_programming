#!/usr/bin/python3
"""Module sends a request to the URL and displays the value"""

import sys
import urllib.request

if __name__ == "__main__":
    # Take the URL from the command-line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    with urllib.request.urlopen(url) as response:
        # Get the headers of the response
        headers = response.info()

        # Print the value of the 'X-Request-Id' variable
        print(headers.get('X-Request-Id'))
