#!/usr/bin/python3
'''function to print # square'''


def print_square(size):
    '''size is the size length of the square'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((('#' * size + '\n') * size), end='')
