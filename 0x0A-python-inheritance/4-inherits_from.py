#!/usr/bin/python3
'''class body '''


def inherits_from(obj, a_class):
    '''true if obj type not equal to a_class'''
    if (issubclass(type(obj), a_class)) and (type(obj) != a_class):
        return (True)
    else:
        return (False)
