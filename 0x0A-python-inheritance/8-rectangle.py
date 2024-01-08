#!/usr/bin/python3
'''rectangle class inherits from BaseGeometry import BaseGeometry class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle class body'''
    def __init__(self, width, height):
        '''init start'''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
