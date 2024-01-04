#!/usr/bin/python3
''' class definition'''


class Square:
    '''class body'''
    def __init__(self, size=0):
        '''init definition
         Raises:
         ValueError: if size is negative
         TypeError: if size is not integer

         Args:
         size:side length
         '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''square area method
        Return: The square area '''
        return self.__size * self.__size
