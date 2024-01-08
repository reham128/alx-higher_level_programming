#!/usr/bin/python3
'''body of class MyInt which inherits from int'''


class MyInt(int):
    '''class to reverse functionallity of equal and not equal'''
    def __eq__(self, input_val):
        '''change == to !=='''
        return (int(self) != input_val)

    def __ne__(self, input_val):
        '''change != to =='''
        return (int(self) == input_val)
