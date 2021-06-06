import pygame

class Screen:

    def __init__(self):
        self.width = 530
        self.height = 580
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((self.width, self.height))
