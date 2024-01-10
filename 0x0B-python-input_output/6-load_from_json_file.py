#!/usr/bin/python3
'''function that creates an Object from a “JSON file”'''


import json


def load_from_json_file(filename):
    '''creat object form JSON file'''
    with open(filename, "r", encoding="utf-8") as file_r:
        return (json.load(file_r))
