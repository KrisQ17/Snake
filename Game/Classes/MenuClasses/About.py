import pygame, os, sys
from Game.Utils.Colors import menuColors

pattayaFont = os.getcwd() + "/Game/assets/Pattaya-Regular.ttf"
arimoFont = os.getcwd() + "/Game/assets/Arimo.ttf"

class About:

    page = "about"

    def __init__(self, surface):
        self.screen = surface

        self.pageNameFont = pygame.font.Font(pattayaFont, 50)
        self.optionFont = pygame.font.Font(arimoFont, 35)
        self.informationFont = pygame.font.Font(arimoFont, 15)

        self.pageName = self.pageNameFont.render("About", True, menuColors['pageName'])
        self.backLabel = self.informationFont.render("Back -> ESC", True, menuColors['navigation'])
        self.text1 = self.informationFont.render("Snake - gra komputerowa, wydana w 1976 roku pod", True, menuColors['description'])
        self.text2 = self.informationFont.render("nazwą 'Blockade'. W grze gracz kontroluje węża, który", True, menuColors['description'])
        self.text3 = self.informationFont.render("stara się zebrać wszystkie oznaczenia znajdujące się", True, menuColors['description'])
        self.text4 = self.informationFont.render("na planszy.", True, menuColors['description'])

    def display(self):
        self.screen.fill(menuColors['background'])
        self.screen.blit(self.pageName, ((self.screen.get_width()-self.pageName.get_width())/2, 10))
        self.screen.blit(self.backLabel, (10, 10))
        self.screen.blit(self.text1, ((self.screen.get_width()-self.text1.get_width())/2, 200))
        self.screen.blit(self.text2, ((self.screen.get_width()-self.text2.get_width())/2, 225))
        self.screen.blit(self.text3, ((self.screen.get_width()-self.text3.get_width())/2, 250))
        self.screen.blit(self.text4, ((self.screen.get_width()-self.text4.get_width())/2, 275))
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.page = "menu"

    def returnPage(self):
        return self.page