#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    # Take the URL from the command-line argument
    url = sys.argv[1]

    try:
        # Send a GET request to the URL
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            body = response.read().decode('utf-8')

            # Print the response body
            print(body)
    except urllib.error.HTTPError as e:
        # Print the HTTP status code
        print('Error code:', e.code)
