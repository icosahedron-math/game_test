from random import randint

from .unit_obj import Unit

class Enemy(Unit):
    def __init__(self, MAP_W, MAP_H, OBJ_SIZE) -> None:
        super().__init__(MAP_W, MAP_H, OBJ_SIZE)
    
    def spawn(self, id_map):
        while True:
            x = randint(0, self.w/self.obj_size-1)
            y = randint(0, self.h/self.obj_size-1)
            if id_map[y][x] not in self.num:
                id_map[y][x] = 2
                self.x = x
                self.y = y
                break
        return id_map