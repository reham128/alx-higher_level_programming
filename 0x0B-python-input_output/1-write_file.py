#!/usr/bin/python3
'''function to creat a file if not exist and overwrite if exist'''


def write_file(filename="", text=""):
    '''write text to a file in utf-8'''
    with open(filename, "w", encoding="utf-8") as file_w:
        return (file_w.write(text))
