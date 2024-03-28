#!/usr/bin/python3
"""take URL, send request, and display val of X-Request-Id variable
found in the header of the response."""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    requ = urllib.request.Request(url)
    with urllib.request.urlopen(requ) as res:
        print(res.headers.get("X-Request-Id"))
