#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, val):
        self.update_int("width", val, False)
        self.__width = val

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, val):
        self.update_int("height", val, False)
        self.__height = val

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, val):
        self.update_int("x", val)
        self.__x = val

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, val):
        self.update_int("y", val)
        self.__y = val

    def update_int(self, n, val, equality=True):
        '''Method for validating the value.'''
        if type(val) != int:
            raise TypeError("{} must be an integer".format(n))
        if equality and val < 0:
            raise ValueError("{} must be >= 0".format(n))
        elif not equality and val <= 0:
            raise ValueError("{} must be > 0".format(n))

    def area(self):
        '''Computes area of this rectangle.'''
        return self.width * self.height

    def display(self):
        '''Prints string representation of this rectangle.'''
        m = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(m, end='')

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self)._name_, self.id, self.x, self.y, self.width,
                   self.height)

    def _update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        # print(args, kwargs)
        if args:
            self._update(*args)
        elif kwargs:
            self._update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
