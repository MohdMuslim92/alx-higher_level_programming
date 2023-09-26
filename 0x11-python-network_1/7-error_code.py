#!/usr/bin/python3
"""
This script sends a request to a URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints the error
code.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: {} <URL>\n".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.status_code)
