#!/usr/bin/python3
""" to take URl , send request, and display body of response"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode("utf-8"))

    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
