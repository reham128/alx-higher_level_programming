#!/usr/bin/python3
''' function that adds 2 integers.'''


def add_integer(a, b=98):
    '''function body'''
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
