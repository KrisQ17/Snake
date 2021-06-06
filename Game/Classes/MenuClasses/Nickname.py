import pygame, os, sys, time

from pygame.constants import KEYDOWN, K_BACKSPACE
from Game.Utils.Colors  import menuColors

pattayaFont = os.getcwd() + "/Game/assets/Pattaya-Regular.ttf"
arimoFont = os.getcwd() + "/Game/assets/Arimo.ttf"

class Nickname():

    def __init__(self, surface, nickname):
        self.page = "nickname"
        self.return_option = ''

        self.screen = surface
        self.nickname = nickname

        self.pageNameFont = pygame.font.Font(pattayaFont, 50)
        self.optionFont = pygame.font.Font(arimoFont, 35)
        self.informationFont = pygame.font.Font(arimoFont, 15)

        self.pageName = self.pageNameFont.render("Nickname", True, menuColors['pageName'])
        self.confirmLabel = self.informationFont.render("Confirm -> Enter", True, menuColors['navigation'])
        self.backLabel = self.informationFont.render("Back -> ESC", True, menuColors['navigation'])
        self.nicknameEditable = self.optionFont.render(self.nickname, True, menuColors['option'])
        self.nicknameRect = self.nicknameEditable.get_rect()
        self.nicknameRect.topleft = ((self.screen.get_width()-self.nicknameEditable.get_width())/2, 220)
        self.maxNicknameLengthLabel = self.informationFont.render("Max 15 letters", True, menuColors['label'])
        self.cursor = pygame.Rect(self.nicknameRect.topright, (3, self.nicknameRect.height))

    def display(self):
        self.screen.fill(menuColors['background'])
        self.screen.blit(self.pageName, ((self.screen.get_width()-self.pageName.get_width())/2, 10))
        self.screen.blit(self.backLabel, (28, 10))
        self.screen.blit(self.confirmLabel, (10, 25))
        self.nicknameRect.topleft = ((self.screen.get_width()-self.nicknameEditable.get_width())/2, 220)
        self.screen.blit(self.nicknameEditable, self.nicknameRect)
        self.screen.blit(self.maxNicknameLengthLabel, ((self.screen.get_width()-self.maxNicknameLengthLabel.get_width())/2, 260))
        if time.time() % 1 > 0.5:
            pygame.draw.rect(self.screen, menuColors['option'], self.cursor)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.return_option = 'back'
                self.page = "menu"
            if keys[pygame.K_RETURN]:
                self.page = "menu"
                self.return_option = "confirm"
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(self.nickname)>0:
                        self.nickname = self.nickname[:-1]
                        self.changeName()
                else:
                    if len(self.nickname)<15:
                        alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm -1234567890'
                        if event.unicode in alphabet:
                            self.nickname += event.unicode
                            self.changeName()

    def changeName(self):
        self.nicknameEditable = self.optionFont.render(self.nickname, True, menuColors['option'])
        self.nicknameRect = self.nicknameEditable.get_rect()
        self.nicknameRect.topleft = ((self.screen.get_width()-self.nicknameEditable.get_width())/2, 220)
        self.cursor = pygame.Rect(self.nicknameRect.topright, (3, self.nicknameRect.height))

    def returnOption(self):
        return self.return_option

    def returnNickname(self):
        if self.nickname == "":
            return "anonymous"
        else:
            return self.nickname