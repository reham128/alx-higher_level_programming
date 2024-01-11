#!/usr/bin/python3
'''to  insert line of text to file
after each line containing a specific string'''


def append_after(filename="", search_string="", new_string=""):
    '''function body'''
    out = ''
    with open(filename, "r", encoding="utf-8") as file_r:
        tmp = file_r.readline()
        for tmp in file_r:
            out += tmp
            if search_string in tmp:
                out += new_string

    with open(filename, "w", encoding="utf-8") as file_w:
        file_w.writelines(out)
