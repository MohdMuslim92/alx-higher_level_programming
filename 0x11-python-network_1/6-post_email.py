#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email parameter and displays
the response body.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: {} <URL> <email>\n".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    dect_email = {'email': email}
    response = requests.post(url, data=dect_email)
    print("Your email is:", email)
