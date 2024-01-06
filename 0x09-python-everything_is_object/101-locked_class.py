#!/usr/bin/python3
'''class to prevents the user from dynamically creating new instance attributes'''


class LockedClass:
    '''class body'''
    __slots__ = ('first_name')
