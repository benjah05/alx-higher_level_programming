#!/usr/bin/python3
"""First class Base"""
import json
import os.path
import csv
import turtle


class Base:
    """Base class of project Almost a circle"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class
        Args:
            id (int): initialize id if arg id is not None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            json_string = "[]"
        else:
            list_listobjs = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_listobjs)
        with open(filename, "w") as json_file:
            json_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Square":
            obj = cls(2)
        if cls.__name__ == "Rectangle":
            obj = cls(2, 4)
        obj.update(**dictionary)
        return (obj)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return ([])
        with open(filename, "r") as json_file:
            json_string = json_file.read()
        json_list = cls.from_json_string(json_string)
        instance_list = [cls.create(**obj_dict) for obj_dict in json_list]
        return (instance_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the csv string representation of list_objs to a file"""
        filename = f"{cls.__name__}.csv"
        if list_objs is None:
            csv_string = "[]"
        else:
            list_listobjs = [obj.to_dictionary() for obj in list_objs]
            csv_string = cls.to_json_string(list_listobjs)
        with open(filename, "w") as csv_file:
            csv_file.write(csv_string)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances"""
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return ([])
        with open(filename, "r") as csv_file:
            csv_string = csv_file.read()
        csv_list = cls.from_json_string(csv_string)
        instance_list = [cls.create(**obj_dict) for obj_dict in csv_list]
        return (instance_list)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draws all the Rectangles and Squares"""
        drawShape = turtle.Turtle()
        drawShape.bgcolor("#CBC3E3")
        drawShape.pensize(3)
        drawShape.shape("turtle")

        drawShape.color("#42249c")
        for rect in list_rectangles:
            drawShape.showturtle()
            drawShape.up()
            drawShape.goto(rect.x, rect.y)
            drawShape.down()
            for i in range(2):
                drawShape.forward(rect.width)
                drawShape.left(90)
                drawShape.forward(rect.height)
                drawShape.left(90)
                drawShape.hideturtle()

        drawShape.color("#11072e")
        for sqr in list_squares:
            drawShape.showturtle()
            drawShape.up()
            drawShape.goto(sqr.x, sqr.y)
            drawShape.down()
            for i in range(2):
                drawShape.forward(sqr.width)
                drawShape.left(90)
                drawShape.forward(sqr.height)
                drawShape.left(90)
                drawShape.hideturtle()

        drawShape.exitonclick()
