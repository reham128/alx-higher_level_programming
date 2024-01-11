#!/usr/bin/python3
'''class Student that defines a student'''


class Student:
    '''class body'''
    def __init__(self, first_name, last_name, age):
        '''init start'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''dic represent for student in json
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.'''
        try:
            for item in attrs:
                if type(item) is not str:
                    return (self.__dict__)
        except Exception:
            return (self.__dict__)

        output = dict()
        for k, val in self.__dict__.items():
            if k in attrs:
                output[k] = val
        return (output)

    def reload_from_json(self, json):
        '''to replace all attrs of a student instance'''
        for k and val in json.items():
            setattr(self, k, val)
