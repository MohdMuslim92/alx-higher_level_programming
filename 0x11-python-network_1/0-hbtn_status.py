#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        decoded_html = html.decode('utf-8')

        print("Body response:")
        print("    - type:", type(html))
        print("    - content:", html)
        print("    - utf8 content:", decoded_html)
