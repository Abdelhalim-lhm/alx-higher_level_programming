#!/usr/bin/python3
''' Square definitionmodule '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square definition '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' sqaure constructor '''
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' str representation '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' update args and kwargs '''
        if args:
            if len(args) >= 1:
                self.id = args[0] if args[0] is not None else self.id
            if len(args) >= 2:
                self.size = args[1] if args[1] is not None else self.size
            if len(args) >= 3:
                self.x = args[2] if args[2] is not None else self.x
            if len(args) >= 4:
                self.y = args[3] if args[3] is not None else self.y

        for key, value in kwargs.items():
            if key == 'id' and value is not None:
                self.id = value
            if key == 'size' and value is not None:
                self.width = value
            if key == 'x' and value is not None:
                self.x = value
            if key == 'y' and value is not None:
                self.y = value

    def to_dictionary(self):
        ''' Dictionnary representation '''
        rect = {'id': self.id, 'x': self.x, 'size': self.size,
                'y': self.y,
                }
        return rect
