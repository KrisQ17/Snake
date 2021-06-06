import pygame, os
from Game.Utils.Tile import Tile
from Game.Utils.Colors import gameColors

snake = os.getcwd() + "/Game/assets/snakesprite.png"

class SnakePart(Tile):

    radius = 9

    def __init__(self, row, column, part, direction):
        super().__init__(row, column)
        self.part = part

        self.directionPicture = direction

        self.snakeSprite = pygame.image.load(snake)

        self.partRotate0 = pygame.transform.rotate(self.snakeSprite, 0)
        self.partRotate90 = pygame.transform.rotate(self.snakeSprite, 90)
        self.partRotate180 = pygame.transform.rotate(self.snakeSprite, 180)
        self.partRotate270 = pygame.transform.rotate(self.snakeSprite, 270)

        self.direction = direction

    def calculateCenter(self, rect):
        return (rect.left+self.radius, rect.top+self.radius)

    def changePart(self, part):
        self.part = part

    def setDirection(self, direction):
        self.direction = direction

    def setDirectionPicture(self, direction):
        self.directionPicture = direction

    def getDirection(self):
        return self.direction

    def displaySnakePart(self, surface):
        if self.part == 'head':
            if self.directionPicture == 'left':
                surface.blit(self.partRotate270, self.rect, (85, 1, 40, 40))
            if self.directionPicture == 'right':
                surface.blit(self.partRotate90, self.rect, (1, 85, 40, 40))
            if self.directionPicture == 'up':
                surface.blit(self.partRotate180, self.rect, (85, 85, 40, 40))
            if self.directionPicture == 'down':
                surface.blit(self.partRotate0, self.rect, (1, 1, 40, 40))
        elif self.part == 'part':
            if self.directionPicture == 'right':
                surface.blit(self.partRotate90, self.rect, (85, 1, 40, 40))
            if self.directionPicture == 'left':
                surface.blit(self.partRotate90, self.rect, (85, 1, 40, 40))
            if self.directionPicture == 'up':
                surface.blit(self.partRotate0, self.rect, (85, 85, 40, 40))
            if self.directionPicture == 'down':
                surface.blit(self.partRotate0, self.rect, (85, 85, 40, 40))
            if self.directionPicture == 'down-right':
                surface.blit(self.partRotate0, self.rect, (43, 43, 40, 40))
            if self.directionPicture == 'down-left':
                surface.blit(self.partRotate0, self.rect, (85, 43, 40, 40))

            if self.directionPicture == 'right-down':
                surface.blit(self.partRotate0, self.rect, (85, 1, 40, 40))
            if self.directionPicture == 'left-down':
                surface.blit(self.partRotate0, self.rect, (43, 1, 40, 40))
            
            if self.directionPicture == 'right-up':
                surface.blit(self.partRotate0, self.rect, (85, 43, 40, 40))
            if self.directionPicture == 'left-up':
                surface.blit(self.partRotate0, self.rect, (43, 43, 40, 40))

            if self.directionPicture == 'up-right':
                surface.blit(self.partRotate0, self.rect, (43, 1, 40, 40))
            if self.directionPicture == 'up-left':
                surface.blit(self.partRotate0, self.rect, (85, 1, 40, 40))
        else:
            if self.directionPicture == 'right':
                surface.blit(self.partRotate270, self.rect, (0, 43, 40, 40))
            if self.directionPicture == 'left':
                surface.blit(self.partRotate90, self.rect, (85, 43, 40, 40))
            if self.directionPicture == 'up':
                surface.blit(self.partRotate0, self.rect, (43, 85, 40, 40))
            if self.directionPicture == 'down':
                surface.blit(self.partRotate180, self.rect, (43, 0, 40, 40))
