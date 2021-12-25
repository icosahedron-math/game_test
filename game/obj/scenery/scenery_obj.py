"""
Global scenery obj
"""
from random import randint

class Scenery():
    def __init__(self, map_w, map_h, obj_size) -> None:
        self.num = [x for x in range(1, 40)]
        self.obj_size = obj_size
        self.w = map_w
        self.h = map_h
        self.id = 0
        self.x = 0
        self.y = 0

    def spawn(self, id_map):
        while True:
            x = randint(0, self.w/self.obj_size-1)
            y = randint(0, self.h/self.obj_size-1)
            if id_map[y][x] not in self.num:
                id_map[y][x] = self.id
                break
        return id_map