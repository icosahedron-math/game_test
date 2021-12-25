"""
Global unit obj
"""

from obj.ids import *


class Unit():
    def __init__(self, map_w, map_h, obj_size) -> None:
        self.obj_size = obj_size
        self.num = [x for x in range(1, 40)]
        self.w = map_w
        self.h = map_h
        self.x = 0
        self.y = 0
    
    def move(self, x, y, id_map):
        if self.x+x not in (self.w/self.obj_size, -1):
            if id_map[self.y][self.x+x] != WALL:
                self.x += x
        if self.y+y not in (self.h/self.obj_size, -1):
            if id_map[self.y+y][self.x] != WALL:
                self.y += y