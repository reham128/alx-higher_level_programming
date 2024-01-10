#!/usr/bin/python3
'''function to append a string at the end of file'''


def append_write(filename="", text=""):
    '''append text to a file in utf-8'''
    with open(filename, "a", encoding="utf-8") as file_a:
        return (file_a.write(text))
