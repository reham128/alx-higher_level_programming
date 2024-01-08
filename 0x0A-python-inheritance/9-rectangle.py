#!/usr/bin/python3
'''rectangle class inherits from BaseGeometry import BaseGeometry class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle class body'''
    def __init__(self, width, height):
        '''init start'''
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def __str__(self):
        '''function to represent str'''
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))

    def area(self):
        '''function to find rectangle area'''
        return (self.__width * self.__height)
