from .unit_obj import Unit

class User(Unit):
    def __init__(self, MAP_W, MAP_H, OBJ_SIZE) -> None:
        super().__init__(MAP_W, MAP_H, OBJ_SIZE)