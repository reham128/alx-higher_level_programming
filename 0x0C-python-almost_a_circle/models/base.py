#!/usr/bin/python3
'''class Bass module'''


class Base:
    ''' class representation'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init start'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
