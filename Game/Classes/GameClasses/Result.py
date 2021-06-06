from Game.Utils.Screen import Screen
import pygame, os, sys, time
from Game.Utils.Colors import menuColors

arimoFont = os.getcwd() + "/Game/assets/Arimo.ttf"
snakeImage = os.getcwd() + "/Game/assets/snake.png"

class Result(Screen):

    def __init__(self, result):
        super().__init__()
        self.optionFont = pygame.font.Font(arimoFont, 35)
        self.optionFont2 = pygame.font.Font(arimoFont, 45)

        self.nickname = result[0]
        self.score = result[1]
        self.difficulty = result[2]
        self.time = result[3]
        self.action = ""


        self.snakeImage = pygame.image.load(snakeImage)
        self.option = 1
        self.optionName = ''
        self.difficultyName = ''
        if self.difficulty == 1:
            self.difficultyName = "Easy"
        elif self.difficulty == 2:
            self.difficultyName = "Medium"
        elif self.difficulty == 3:
            self.difficultyName = "Hard"
        self.timeToText = time.strftime('%H:%M:%S', time.gmtime(self.time))

        self.nicknameLabel = self.optionFont.render("Congratulations " + self.nickname + "!", True, menuColors['pauseNormal'])
        self.scoreLabel = self.optionFont.render("Your score: " + str(self.score), True, menuColors['pauseNormal'])
        self.timeLabel = self.optionFont.render("In time: " + self.timeToText, True, menuColors['pauseNormal'])
        self.difficultyLabel = self.optionFont.render("Difficulty: " + self.difficultyName, True, menuColors['pauseNormal'])
        self.backToMenuOption = self.optionFont2.render("Back to menu", True, menuColors['pauseNormal'])
        self.exitOption = self.optionFont.render("Exit", True, menuColors['pauseSelected'])

    def display(self):
        self.screen.fill(menuColors['backgroundResult'])
        self.screen.blit(self.snakeImage, ((self.screen.get_width()-self.snakeImage.get_width())/2, 40))
        self.screen.blit(self.nicknameLabel, ((self.screen.get_width()-self.nicknameLabel.get_width())/2, 200))
        self.screen.blit(self.scoreLabel, ((self.screen.get_width()-self.scoreLabel.get_width())/2, 240))
        self.screen.blit(self.timeLabel, ((self.screen.get_width()-self.timeLabel.get_width())/2, 280))
        self.screen.blit(self.backToMenuOption, ((self.screen.get_width()-self.backToMenuOption.get_width())/2, 350))
        self.screen.blit(self.exitOption, ((self.screen.get_width()-self.exitOption.get_width())/2, 420))
        pygame.display.update()

    def changeOption(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.option != 1:
                self.option -= 1
        if keys[pygame.K_DOWN]:
            if self.option != 2:
                self.option += 1
        if self.option == 1:
            self.backToMenuOption = self.optionFont2.render("Back to menu", True, menuColors['pauseSelected'])
            self.exitOption = self.optionFont.render("Exit", True, menuColors['pauseNormal'])
        if self.option == 2:
            self.backToMenuOption = self.optionFont.render("Back to menu", True, menuColors['pauseNormal'])
            self.exitOption = self.optionFont2.render("Exit", True, menuColors['pauseSelected'])

    def selectOption(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if self.option == 1:
                self.action = "menu"
                self.optionName = 'menu'
                self.running = False
            if self.option == 2:
                self.action = "exit"
                self.optionName = 'exit'
                self.running = False

    def eventsHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.changeOption()
            self.selectOption()

    def returnAction(self):
        return self.action

    def run(self):
        self.running = True
        while self.running:
            self.eventsHandler()
            self.display()