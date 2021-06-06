import pygame, os, sys
from Game.Utils.Colors import menuColors

pattayaFont = os.getcwd() + "/Game/assets/Pattaya-Regular.ttf"
arimoFont = os.getcwd() + "/Game/assets/Arimo.ttf"

class Difficulty:

    def __init__(self, surface, difficulty_option):
        self.page = "difficulty"
        self.return_option = ''
        self.screen = surface
        self.option = difficulty_option

        self.pageNameFont = pygame.font.Font(pattayaFont, 50)
        self.optionFont = pygame.font.Font(arimoFont, 35)
        self.descriptionFont = pygame.font.Font(arimoFont, 20)
        self.informationFont = pygame.font.Font(arimoFont, 15)

        self.pageName = self.pageNameFont.render("Difficulty", True, menuColors['pageName'])
        self.backLabel = self.informationFont.render("Back -> ESC", True, menuColors['navigation'])
        self.confirmLabel = self.informationFont.render("Confirm -> Enter", True, menuColors['navigation'])
        self.arrowLeft = self.optionFont.render("<", True, menuColors['navigation'])
        self.arrowRight = self.optionFont.render(">", True, menuColors['navigation'])
        self.changeOption(self.option)
        self.descriptionLabel = self.descriptionFont.render("Description:", True, menuColors['description'])

    def display(self):
        self.screen.fill(menuColors['background'])
        if self.option == 1:
            self.screen.blit(self.arrowLeft, ((self.screen.get_width()-self.difficultyOption.get_width())/2-60, 150))
            self.screen.blit(self.difficultyOption, ((self.screen.get_width()-self.difficultyOption.get_width())/2, 150))
            self.screen.blit(self.arrowRight, (((self.screen.get_width()-self.difficultyOption.get_width())/2)+self.difficultyOption.get_width()+40, 150))
            self.speedLabel = self.informationFont.render("SPEED: 400ms", True, menuColors['text'])
            self.scoreLabel = self.informationFont.render("SCORE: 10 points for food", True, menuColors['text'])
            self.extrasLabel = self.informationFont.render("EXTRAS: None", True, menuColors['text'])
            self.extrasLabel2 = self.informationFont.render("", True, menuColors['text'])
        if self.option == 2:
            self.screen.blit(self.arrowLeft, ((self.screen.get_width()-self.difficultyOption.get_width())/2-60, 150))
            self.screen.blit(self.difficultyOption, ((self.screen.get_width()-self.difficultyOption.get_width())/2, 150))
            self.screen.blit(self.arrowRight, (((self.screen.get_width()-self.difficultyOption.get_width())/2)+self.difficultyOption.get_width()+40, 150))
            self.speedLabel = self.informationFont.render("SPEED: 300ms", True, menuColors['text'])
            self.scoreLabel = self.informationFont.render("SCORE: 15 points * multiplier of type food", True, menuColors['text'])
            self.extrasLabel = self.informationFont.render("EXTRAS: 2 types of food (apple - x1, broccoli - x2)", True, menuColors['text'])
            self.extrasLabel2 = self.informationFont.render("", True, menuColors['text'])
        if self.option == 3:
            self.screen.blit(self.arrowLeft, ((self.screen.get_width()-self.difficultyOption.get_width())/2-60, 150))
            self.screen.blit(self.difficultyOption, ((self.screen.get_width()-self.difficultyOption.get_width())/2, 150))
            self.screen.blit(self.arrowRight, (((self.screen.get_width()-self.difficultyOption.get_width())/2)+self.difficultyOption.get_width()+40, 150))
            self.speedLabel = self.informationFont.render("SPEED: from 300ms to 100ms - increases over time", True, menuColors['text'])
            self.scoreLabel = self.informationFont.render("SCORE: 20 points * multiplier of type food + 100 points every 20s", True, menuColors['text'])
            self.extrasLabel = self.informationFont.render("EXTRAS: 3 types of food (apple - x1, broccoli - x2, hamburger - x3)", True, menuColors['text'])
            self.extrasLabel2 = self.informationFont.render("+ random walls", True, menuColors['text'])

        self.screen.blit(self.pageName, ((self.screen.get_width()-self.pageName.get_width())/2, 10))
        self.screen.blit(self.backLabel, (28, 10))
        self.screen.blit(self.confirmLabel, (10, 25))

        self.screen.blit(self.descriptionLabel, (40, 300))
        self.screen.blit(self.speedLabel, (40, 340))
        self.screen.blit(self.scoreLabel, (40, 370))
        self.screen.blit(self.extrasLabel, (40, 400))
        self.screen.blit(self.extrasLabel2, (105, 415))

        pygame.display.update()

    def changeOption(self, number):
        if number == 1:
            self.difficultyOption = self.optionFont.render("Easy", True, menuColors['option'])
        if number == 2:
            self.difficultyOption = self.optionFont.render("Medium", True, menuColors['option'])
        if number == 3:
            self.difficultyOption = self.optionFont.render("Hard", True, menuColors['option'])

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.page = "menu"
                self.return_option = "back"
            if keys[pygame.K_LEFT]:
                self.option -= 1
                if self.option == 0:
                    self.option = 3
                self.changeOption(self.option)
            if keys[pygame.K_RIGHT]:
                self.option += 1
                if self.option == 4:
                    self.option = 1
                self.changeOption(self.option)
            if keys[pygame.K_RETURN]:
                self.page = "menu"
                self.return_option = "confirm"

    def returnOption(self):
        return self.return_option

    def returnDifficultyOption(self):
        return self.option