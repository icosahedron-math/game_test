from obj.ids import WALL
from .scenery_obj import Scenery

class Wall(Scenery):
    def __init__(self, MAP_W, MAP_H, OBJ_SIZE) -> None:
        super().__init__(MAP_W, MAP_H, OBJ_SIZE)
        self.id = WALL