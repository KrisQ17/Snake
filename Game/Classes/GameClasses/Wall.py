from random import randint
import pygame, os
from Game.Utils.Tile import Tile
from Game.Utils.Colors import gameColors

tile_x1 = os.getcwd() + "/Game/assets/wall.png"

class Wall():

    def __init__(self):
        self.walls = []
        self.tile01 = pygame.image.load(tile_x1)
        self.tile01 = pygame.transform.scale(self.tile01, (40, 40))
        self.generateWall()

    def generateWall(self):
        column = randint(0, 10)
        row = randint(0, 10)
        direction = randint(0, 1)
        tile1 = Tile(row, column)
        if direction == 0:
            tile2 = Tile(row+1, column)
            tile3 = Tile(row+2, column)
        if direction == 1:
            tile2 = Tile(row, column+1)
            tile3 = Tile(row, column+2)
        self.walls.append(tile1)
        self.walls.append(tile2)
        self.walls.append(tile3)

    def display(self, surface):
        for w in self.walls:
            #pygame.draw.rect(surface, gameColors['black'], w.getRect(), 0)
            surface.blit(self.tile01, w.getRect())

    def collide(self, tile):
        collide = False
        for w in self.walls:
            if w.isCollide(tile):
                collide = True
        return collide




