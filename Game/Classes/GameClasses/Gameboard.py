import pygame
from Game.Utils.Colors import gameColors

class Gameboard:

    blockSize = 40

    def __init__(self, left, top, width, height):
        self.rect = pygame.Rect(left, top, width, height)

    def display(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)
        self.drawGrid(surface)

    def drawGrid(self, screen):
        row = 0
        column = 0
        for x in range(5, self.rect.width, self.blockSize):
            for y in range(0, self.rect.height, self.blockSize):
                if row % 2 == 0 and column % 2  == 0:
                    rect = pygame.Rect(x, self.rect.topleft[1] + y, self.blockSize, self.blockSize)
                    pygame.draw.rect(screen, gameColors['tile1'], rect)
                    column += 1
                elif row % 2 != 0 and column %2 != 0:
                    rect = pygame.Rect(x, self.rect.topleft[1] + y, self.blockSize, self.blockSize)
                    pygame.draw.rect(screen, gameColors['tile1'], rect)
                    column += 1
                else:
                    rect = pygame.Rect(x, self.rect.topleft[1] + y, self.blockSize, self.blockSize)
                    pygame.draw.rect(screen, gameColors['tile2'], rect)
                    column += 1
            column = 0
            row += 1