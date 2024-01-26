#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Take the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email
    values = {'email': email}

    # Encode the dictionary into URL parameters
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes

    # Send a POST request to the URL with the email parameter
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')

        # Print the response body
        print(body)
