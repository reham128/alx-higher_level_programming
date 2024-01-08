#!/usr/bin/python3
''' class module'''


def is_kind_of_class(obj, a_class):
    '''returns True if the object is an instance'''
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
