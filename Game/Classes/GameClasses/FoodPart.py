import pygame, os
from Game.Utils.Tile import Tile
from Game.Utils.Colors import gameColors

tile_x1 = os.getcwd() + "/Game/assets/tile1.png"
tile_x2 = os.getcwd() + "/Game/assets/tile2.png"
tile_x3 = os.getcwd() + "/Game/assets/tile3.png"

class FoodPart(Tile):

    def __init__(self, row, column, typeFood):
        super().__init__(row, column)
        self.typeFood = typeFood
        self.blockSize = 20

        self.tile01 = pygame.image.load(tile_x1)
        self.tile01 = pygame.transform.scale(self.tile01, (40, 40))

        self.tile02 = pygame.image.load(tile_x2)
        self.tile02 = pygame.transform.scale(self.tile02, (40, 40))

        self.tile03 = pygame.image.load(tile_x3)
        self.tile03 = pygame.transform.scale(self.tile03, (40, 40))


    def calculatePolygon(self, rect):
        top = rect.top
        left = rect.left
        return [(left+2, top + self.blockSize/2), (left+self.blockSize/2, top+2), 
                (left + self.blockSize - 2, top + self.blockSize/2),
                (left+self.blockSize/2, top + self.blockSize - 2)]

    def display(self, surface):
        if self.typeFood == 1:
            #pygame.draw.polygon(surface, gameColors['food1'], self.calculatePolygon(self.rect), 0)
            surface.blit(self.tile01, self.rect)
            #surface.blit(self.test, self.rect, (0, 0, 40, 40))
        elif self.typeFood == 2:
            surface.blit(self.tile02, self.rect)
        elif self.typeFood == 3:
            surface.blit(self.tile03, self.rect)

    def returnTypeFood(self):
        return self.typeFood