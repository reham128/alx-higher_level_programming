#!/usr/bin/python3
'''body of class MyInt which inherits from int'''


class MyInt(int):
    '''class to reverse functionallity of equal and not equal'''
    def __eq__(self, value):
        '''change == to !=='''
        return (self.real != value)

    def __ne__(self, value):
        '''change != to =='''
        return (self.real == value)
