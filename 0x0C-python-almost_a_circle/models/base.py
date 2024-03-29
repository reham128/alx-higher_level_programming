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
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new_inc = Rectangle(1, 1)
        elif cls is Square:
            new_inc = Square(1)
        else:
            new_inc = None
        new_inc.update(**dictionary)
        return (new_inc)

    @classmethod
    def load_from_file(cls):
        '''to return list of instances'''
        f_name = "{}.json".format(cls.__name__)

        if os.path.exists(f_name) is False:
            return []
        with open(f_name, "r", encoding="utf-8") as f:
            tmp = f.read()

        clss_list = cls.from_json_string(tmp)
        instance_list = []

        for i in range(len(clss_list)):
            instance_list.append(cls.create(**clss_list[i]))

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''serializes in CSV'''
        f_name = "{}.csv".format(cls.__name__)

        with open(f_name, "w", newLine="") as fcsv:
            if list_objs is None or list_objs == []:
                fcsv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    oblist = ['id', 'width', 'height', 'x', 'y']
                else:
                    oblist = ['id', 'size', 'x', 'y']
                new = csv.DictWriter(fcsv, oblist=oblist)
                for ob in list_objs:
                    new.writerow(ob.to_dictionary())
