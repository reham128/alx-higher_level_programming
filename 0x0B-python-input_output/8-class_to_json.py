#!/usr/bin/python3
'''python object serialization to json'''


def class_to_json(obj):
    '''to return dic description with simple data structure'''
    return (obj.__dict__)
