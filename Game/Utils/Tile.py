import pygame

class Tile:

    width = 5
    height = 55
    blockSize = 40

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.rect = pygame.Rect(self.width + (self.column*self.blockSize), 
                                self.height + (self.row*self.blockSize),
                                self.blockSize, self.blockSize)
        self.coords = [row, column]

    def getCoords(self):
        return self.coords

    def setPosition(self, row, column):
        self.rect = pygame.Rect(self.width + (column*self.blockSize), 
                                    self.height + (row*self.blockSize),
                                    self.blockSize, self.blockSize)

        self.coords = [row, column]

    def getRect(self):
        return self.rect

    def isCollide(self, tile):
        x_1 = self.coords[0]
        y_1 = self.coords[1]
        x_2 = tile.getCoords()[0]
        y_2 = tile.getCoords()[1]
        if x_1 == x_2 and y_1 == y_2:
            return True

