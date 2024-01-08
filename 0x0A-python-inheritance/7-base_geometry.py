#!/usr/bin/python3
'''empyt class body'''


class BaseGeometry:
    '''class start'''
    def area(self):
        '''empyt'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''function to validates value and raise exception errors'''
        if (type(value) != int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
