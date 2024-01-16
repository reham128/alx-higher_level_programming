#!/usr/bin/python3
'''class Rectangle inherit form base super class'''


from models.base import Base


class Rectangle(Base):
    '''class impelementation'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''init start'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''set/get of rectangle width'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''set/get of rectangle height'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''set/get of x'''
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        '''set/get of y'''
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        '''find rect area'''
        return (self.width * self.height)

    def display(self):
        '''to print rectangle using # to stdout'''
        rec = '\n' * self.y
        for i in range(self.height):
            rec += (' ' * self.x)
            rec += ('#' * self.width) + '\n'

        print(rec, end='')

    def __str__(self):
        '''method str to representation'''
        str_rec = "[Rectangle]"
        str_id = "({}) ".format(self.id)
        str_x_y = "{}/{} - ".format(self.x, self.y)
        str_w_h = "{}/{}".format(self.width, self.height)

        return str_rec + str_id + str_x_y + str_w_h

    def update(self, *args, **kwargs):
        '''*args and **kwargs'''
        if len(args) == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
