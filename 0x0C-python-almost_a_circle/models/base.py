#!/usr/bin/python3
'''class Bass module'''
import json
import csv
import os.path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        f_name = cls.__name__ + ".json"
        with open(f_name, "w") as filejson:
            if list_objs is None:
                filejson.write("[]")
            else:
                dic_list = [obj.to_dictionary() for obj in list_objs]
                filejson.write(Base.to_json_string(dic_list))
