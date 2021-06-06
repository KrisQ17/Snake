import pygame, os, sys
from Game.Utils.Colors import menuColors

arimoFont = os.getcwd() + "/Game/assets/Arimo.ttf"

class Pause:

    def __init__(self, screen, pause):
        self.optionFont = pygame.font.Font(arimoFont, 35)
        self.optionFont2 = pygame.font.Font(arimoFont, 45)

        self.screen = screen
        self.pause = pause

        self.option = 1
        self.optionName = ''
        
        self.resumeOption = self.optionFont2.render("Resume", True, menuColors['pauseSelected'])
        self.backToMenuOption = self.optionFont.render("Back to menu", True, menuColors['pauseNormal'])

    def display(self, surface):
        surface.blit(self.resumeOption, ((self.screen.get_width()-self.resumeOption.get_width())/2, 150))
        surface.blit(self.backToMenuOption, ((self.screen.get_width()-self.backToMenuOption.get_width())/2, 230))

    def changeOption(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.option != 1:
                self.option -= 1
        if keys[pygame.K_DOWN]:
            if self.option != 2:
                self.option += 1
        if self.option == 1:
            self.resumeOption = self.optionFont2.render("Resume", True, menuColors['pauseSelected'])
            self.backToMenuOption = self.optionFont.render("Back to menu", True, menuColors['pauseNormal'])
        if self.option == 2:
            self.resumeOption = self.optionFont.render("Resume", True, menuColors['pauseNormal'])
            self.backToMenuOption = self.optionFont2.render("Back to menu", True, menuColors['pauseSelected'])

    def selectOption(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if self.option == 1:
                self.pause = False
                self.optionName = 'resume'
            if self.option == 2:
                self.pause = False
                self.optionName = 'menu'

    def getOption(self):
        return self.optionName

    def eventsHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.changeOption()
            self.selectOption()