#!/usr/bin/python3
''' function that adds a new attribute to an object if it’s possible'''


def add_attribute(objec, atteribu, val):
    '''method to add new atteribute to object'''
    if not hasattr(objec, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(objec, atteribu, val)
