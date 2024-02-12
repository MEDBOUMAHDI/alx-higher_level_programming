#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads
import csv


class Base:
    '''A representation of the base of our OOP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
     @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Unjsonifies a dictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jsonified object to file.'''
        if list_objs is not None:
            list_objs = [ob.to_dictionary() for ob in list_objs]
        with open("{}.json".format(cls._name_), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            n = Rectangle(1, 1)
        elif cls is Square:
            n = Square(1)
        else:
            n = None
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        from os import path
        f = "{}.json".format(cls._name_)
        if not path.isfile(f):
            return []
        with open(f, "r", encoding="utf-8") as fi:
            return [cls.create(**dir) for dir in cls.from_json_string(f.read())]
    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[ob.id, ob.width, ob.height, ob.x, ob.y]
                             for ob in list_objs]
            else:
                list_objs = [[ob.id, ob.size, ob.x, ob.y]
                             for ob in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)
    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    a = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    a = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**a))
        return ret
