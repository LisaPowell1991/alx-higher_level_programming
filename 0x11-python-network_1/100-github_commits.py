#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"

    response = requests.get(url)

    repo_data = response.json()
