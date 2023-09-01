#!/usr/bin/python3
"""
This script uses the GitHub API to list 10 commits from a repository by
a specific user.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write(
                "Usage: {} <Repo name> <owner_name\n".format(sys.argv[0]))
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    parameters = {'per_page': 10}
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author}")
    else:
        print("Error: Unable to retrieve commits.")
