#!/usr/bin/python3
'''class Student that defines a student'''


class Student:
    '''class body'''
    def __init__(self, first_name, last_name, age):
        '''init start'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''dic represent for student in json'''
        return (self.__dict__)
