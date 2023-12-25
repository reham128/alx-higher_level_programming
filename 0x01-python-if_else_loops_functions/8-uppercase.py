#!/usr/bin/python3
def uppercase(str):
    output = ""
    for case in str:
        value = case
        if ord(value) >= 97 and ord(value) <= 123:
            value = chr(ord(case) - 32)
        print("{}".format(value), end="")
    print('')
