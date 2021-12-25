from random import randint
import pygame

from obj import *

MAP_W = 800
MAP_H = 800
OBJ_SIZE = 20


class Main():
    def __init__(self) -> None:
        pygame.init()
        # def window
        self.wim = pygame.display.set_mode((MAP_W, MAP_H))
        pygame.display.set_caption("Kklmao test game")

        # settings
        self.fps = pygame.time.Clock()
        self.wall_color = 0
        self.wall_color_time = 0
        self.enemy_move_tick = 0

        # make obj
        self.user = User(MAP_W, MAP_H, OBJ_SIZE)
        self.enemy = Enemy(MAP_W, MAP_H, OBJ_SIZE)
        self.wall = Wall(MAP_W, MAP_H, OBJ_SIZE)
        self.wall.id = WALL

        # make id map
        self.IdMapDefer()

    def IdMapDefer(self):
        self.id_map = []
        for _ in range(int(MAP_H/OBJ_SIZE)):
            row = []
            for __ in range(int(MAP_W/OBJ_SIZE)):
                row.append(SP)
            self.id_map.append(row)
        self.id_map[0][0] = USER

        # enemy spawn
        self.id_map = self.enemy.spawn(self.id_map)

        # wall spawn
        for _ in range(40):
            self.id_map = self.wall.spawn(self.id_map)

    def WallColorChange(self):
        if self.wall_color_time == 0:
            self.wall_color+=1
            if self.wall_color == 200:
                self.wall_color_time = 1
        if self.wall_color_time == 1:
            self.wall_color-=1
            if self.wall_color == 100:
                self.wall_color_time = 0

    def IdMapUpdate(self):
        # update obj
        y_id = 0
        for y in self.id_map:
            x_id = 0
            for x in y:
                move = True
                if x == USER:
                    if self.id_map[self.user.y][self.user.x] == ENEMY:
                        self.id_map[self.user.y][self.user.x] = SP
                        self.id_map = self.enemy.spawn(self.id_map)
                    
                    elif self.id_map[self.user.y][self.user.x] == WALL:
                        move = False

                    if move:
                        self.id_map[y_id][x_id], self.id_map[self.user.y][self.user.x] = self.id_map[self.user.y][self.user.x], self.id_map[y_id][x_id]
                elif x == ENEMY:
                    if self.id_map[self.enemy.y][self.enemy.x] in self.enemy.num:
                        move = False

                    if move:
                        self.id_map[y_id][x_id], self.id_map[self.enemy.y][self.enemy.x] = self.id_map[self.enemy.y][self.enemy.x], self.id_map[y_id][x_id]
                x_id += 1
            y_id += 1

    def WindowUpdate(self):
        self.wim.fill((0, 0, 0))
        y_id = 0
        for y in self.id_map:
            x_id = 0
            for x in y:
                if x == USER:
                    pygame.draw.rect(self.wim, (0, 0, 255), (x_id*OBJ_SIZE, y_id*OBJ_SIZE, OBJ_SIZE, OBJ_SIZE))
                elif x == ENEMY:
                    pygame.draw.rect(self.wim, (255, 0, 0), (x_id*OBJ_SIZE, y_id*OBJ_SIZE, OBJ_SIZE, OBJ_SIZE))
                elif x == WALL:
                    pygame.draw.rect(self.wim, (0, self.wall_color, 0), (x_id*OBJ_SIZE, y_id*OBJ_SIZE, OBJ_SIZE, OBJ_SIZE))
                x_id += 1
            y_id += 1
        pygame.display.flip()

    def interface(self):
        worked = True
        while worked:
            for event in pygame.event.get():
                # проверить закрытие окна
                if event.type == pygame.QUIT:
                    worked = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        self.user.move(-1, 0, self.id_map)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.user.move(1, 0, self.id_map)
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self.user.move(0, -1, self.id_map)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.user.move(0, 1, self.id_map)
            self.IdMapUpdate()
            self.WallColorChange()
            self.WindowUpdate()
            self.enemy_move_tick += 1
            if self.enemy_move_tick == 15:
                self.enemy.move(randint(-1, 1), randint(-1, 1), self.id_map)
                self.enemy_move_tick = 0
            self.fps.tick(60)


if __name__ == '__main__':
    main = Main()
    main.interface()