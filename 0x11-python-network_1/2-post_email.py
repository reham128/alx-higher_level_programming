#!/usr/bin/python3
"""To send POST request to URL with given ema"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode('utf-8')
    requ = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(requ) as res:
        print(res.read().decode('utf-8'))
