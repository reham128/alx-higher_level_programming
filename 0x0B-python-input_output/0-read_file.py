#!/usr/bin/python3
''' function to read a file and print it to stdout'''


def read_file(filename=""):
    '''read the file in utf-8'''
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
