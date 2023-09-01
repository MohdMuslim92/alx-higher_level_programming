#!/usr/bin/python3
"""
This script uses the GitHub API to display your id using Basic Authentication
with a personal access token.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write(
                "Usage: {} <github user> <github pass\n".format(sys.argv[0]))
        sys.exit(1)

    user = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(user, token))
    if response.status_code == 200:
        data = response.json()
        print(data.get("id"))
    else:
        print("None")
