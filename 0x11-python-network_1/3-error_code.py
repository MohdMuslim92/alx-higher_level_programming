#!/usr/bin/python3
"""
This script sends a request to a URL and displays the body of the response
(decoded in utf-8).
It handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: {} <URL>\n".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        sys.stderr.write("Error code: {}\n".format(str(e.code)))
        sys.exit(1)
    except Exception as e:
        sys.stderr.write("Error: {}\n".format(str(e)))
        sys.exit(1)
