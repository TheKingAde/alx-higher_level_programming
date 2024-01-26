#!/usr/bin/python3
"""Function fetches finacial data"""
import urllib.request


def fetch_data():
    """Function fetches financial data"""
    # Specify the URL
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request to the URL
    with urllib.request.urlopen(url) as response:
        # Read the response body
        body = response.read()

        # Display the body response
        print('Body response:')
        print('\t- type:', type(body))
        print('\t- content:', body)
        print('\t- utf8 content:', body.decode('utf-8'))


if __name__ == "__main__":
    fetch_data()
