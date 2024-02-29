#!/usr/bin/python3
"""Python script that takes your GitHub credentials
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    # Take the username and token from the command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # Specify the URL of the GitHub API
    url = 'https://api.github.com/user'

    # Send a GET request to the URL with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # Parse the JSON response
    data = response.json()

    # Print the user id
    print(data.get('id'))
