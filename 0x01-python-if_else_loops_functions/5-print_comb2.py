#!/usr/bin/python3
for dig in range(100):
    if dig != 99:
        print("{:02d}, ".format(dig), end='')
    else:
        print("{}".format(dig))
