#!/usr/bin/python3
''' class Rectangle definition'''


class Rectangle:
    ''' class body'''
    def __init__(self, width=0, height=0):
        '''init method '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''getter of width'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''setter of width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''getter of height'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''calc rect area'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''calc rect perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
