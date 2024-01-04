#!/usr/bin/python3
''' class definition'''


class Square:
    '''class body'''
    def __init__(self, size=0):
        '''init start'''
        self.size = size

    @property
    def size(self):
        ''' to find sqr size '''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''sqr area method'''
        return self.__size * self.__size
