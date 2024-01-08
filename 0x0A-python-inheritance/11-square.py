#!/usr/bin/python3
'''square class module that inherits from Rectangle'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''square class start'''

    def __init__(self, size):
        '''init start'''
        super().integer_validator('size', size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        '''to finde rectangle area'''
        return (self.__size ** 2)

    def __str__(self):
        '''to represent output'''
        return ('[Square] {}/{}'.format(self.__size, self.__size))
