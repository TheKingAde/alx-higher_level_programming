#!/usr/bin/python3
"""
list 10 commits (most recent to oldest) of the repo “rails” by the user “rails”
"""
import requests
import sys

if __name__ == "__main__":
    # Take the repository name and owner name
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Specify the URL of the GitHub API
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()

    # Print the SHA and author name of each commit
    for commit in data[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
