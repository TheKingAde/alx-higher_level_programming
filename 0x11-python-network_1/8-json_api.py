#!/usr/bin/python3
"""Python script takes in a letter and sends a POST request"""

import requests
import sys

if __name__ == '__main__':
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    url = 'http://0.0.0.0:5000/search_user'

    values = {'q': letter}

    response = requests.post(url, data=values)

    try:
        data = response.json()

        if not data:
            print('No result')
        else:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
    except ValueError:
        print('Not a valid JSON')
