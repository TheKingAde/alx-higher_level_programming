#!/usr/bin/python3
"""Python Script takes in a URL and an email address,
sends a POST request to the passed URL with the email
as a parameter and finally displays the body of thr response"""

import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}

    response = requests.post(url, data=values)

    print(response.text)
