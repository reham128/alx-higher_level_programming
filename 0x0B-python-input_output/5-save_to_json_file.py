#!/usr/bin/python3
'''function that writes an Object to a text file,
using a JSON representation'''


import json


def save_to_json_file(my_obj, filename):
    '''write object to txt file using json'''
    with open(filename, "w") as file_w:
        json.dump(my_obj, file_w)
