#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email parameter and displays
the response body.
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: {} <URL> <email>\n".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data)

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except Exception as e:
        sys.stderr.write("Error: {}\n".format(str(e)))
        sys.exit(1)
