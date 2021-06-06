import pygame
import time
from Game.Utils.Colors import gameColors

class Scoreboard:

    def __init__(self, nickname, left, top, width, height):
        pygame.init()
        self.fontNick = pygame.font.SysFont('Arial', 18)
        self.font = pygame.font.SysFont('Arial', 25)
        self.rect = pygame.Rect(left, top, width, height)
        self.score = 0
        self.time = 0
        self.nickname = nickname
        self.timeText = time.strftime('%H:%M:%S', time.gmtime(self.time))

    def display(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)
        self.addNicknameText(surface)
        self.addScoreText(surface)
        self.addScoreNumber(surface)
        self.addTimeElapsed(surface)
        self.addTimeNumber(surface)

    def addSecond(self):
        self.time += 1
        self.timeText = time.strftime('%H:%M:%S', time.gmtime(self.time))

    def getTimeInSeconds(self):
        return self.time

    def addScore(self, difficulty, foodType):
        if difficulty == 1:
            self.score += 10
        elif difficulty == 2:
            scoreTemp = 15 * foodType
            self.score += scoreTemp
        elif difficulty == 3:
            scoreTemp = 20 * foodType
            self.score += scoreTemp

    def addScoreForTime(self, score):
        self.score += score

    def addNicknameText(self, surface):
        surface.blit(self.fontNick.render(self.nickname, True, gameColors['scoreText']), (30, 15))

    def addTimeNumber(self, surface):
        surface.blit(self.font.render(self.timeText, True, gameColors['scoreText']), (425, 10))

    def addTimeElapsed(self, surface):
        surface.blit(self.font.render("Time:", True, gameColors['scoreText']), (370, 10)) 

    def addScoreText(self, surface):
        surface.blit(self.font.render("Score:", True, gameColors['scoreText']), (200, 10)) 
    
    def addScoreNumber(self, surface):
        surface.blit(self.font.render(str(self.score), True, gameColors['scoreNumber']), (260, 10)) 