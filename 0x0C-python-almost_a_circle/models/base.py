#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        fname = cls.__name__ + ".json"
        with open(fname, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [ob.to_dictionary() for ob in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                n = cls(1, 1)
            else:
                n = cls(1)
            n.update(**dictionary)
            return n

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**m) for m in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        fname = cls.__name__ + ".csv"
        with open(fname, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fildnames = ["id", "width", "height", "x", "y"]
                else:
                    fildnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fildnames=fildnames)
                for ob in list_objs:
                    writer.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        fname = cls.__name__ + ".csv"
        try:
            with open(fname, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fildnames = ["id", "width", "height", "x", "y"]
                else:
                    fildnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fildnames=fildnames)
                list_dicts = [dict([l, int(m)] for l, m in b.items())
                              for b in list_dicts]
                return [cls.create(**b) for b in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rect, list_squ):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        tu = turtle.Turtle()
        tu.screen.bgcolor("#b7312c")
        tu.pensize(3)
        tu.shape("turtle")

        tu.color("#ffffff")
        for rectan in list_rect:
            tu.showturtle()
            tu.up()
            tu.goto(rectan.x, rectan.y)
            tu.down()
            for j in range(2):
                tu.forward(rectan.width)
                tu.left(90)
                tu.forward(rectan.height)
                tu.left(90)
            tu.hideturtle()

        tu.color("#b5e3d8")
        for squ in list_squ:
            tu.showturtle()
            tu.up()
            tu.goto(squ.x, squ.y)
            tu.down()
            for j in range(2):
                tu.forward(squ.width)
                tu.left(90)
                tu.forward(squ.height)
                tu.left(90)
            tu.hideturtle()

        turtle.exitonclick()
