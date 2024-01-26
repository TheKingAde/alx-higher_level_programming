#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import requests


def fetch_data():
    """function fetches https://alx-intranet.hbtn.io/status"""
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the type and content of the response
    print('Body response:')
    print('\t- type:', type(response.text))
    print('\t- content:', response.text)


if __name__ == "__main__":
    fetch_data()
