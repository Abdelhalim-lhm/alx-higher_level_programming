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
