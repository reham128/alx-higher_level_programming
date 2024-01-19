#!/usr/bin/python3
'''square class representation'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class of square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''init start'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''override str method'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        '''set/get square size'''
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

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
