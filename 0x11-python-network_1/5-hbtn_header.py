#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays the value of the
variable X-Request-Id in the response header"""
import requests
import sys

if __name__ == "__main__":
    # Take the URL from the command-line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the value of the 'X-Request-Id' variable
    print(response.headers.get('X-Request-Id'))
