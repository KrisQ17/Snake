from Game.Classes.GameClasses.Result import Result
from Game.Classes.GameClasses.Pause import Pause
from Game.Utils.Screen import Screen
from Game.Classes.GameClasses.Wall import Wall
from Game.Classes.GameClasses.Food import Food
import pygame, sys
from Game.Classes.GameClasses.Scoreboard import Scoreboard
from Game.Classes.GameClasses.Gameboard import Gameboard
from Game.Classes.GameClasses.Snake import Snake
from Game.Utils.Colors import gameColors
import random

class Game(Screen):

    def __init__(self, screen, nickname, difficulty):
        self.lastActionTime = 0
        self.timeElapsed = 0
        self.timeElapsedExtra = 0
        self.screen = screen
        self.second = 1000
        self.nickname = nickname
        self.difficulty = difficulty
        self.pause = False
        self.endGame = False
        self.running = True
        self.action = ''

        self.scoreboard = Scoreboard(nickname, 0, 0, 530, 50)
        self.gameboard = Gameboard(5, 55, 500, 500)
        self.walls = []
        self.snake = Snake()
        self.setDifficultySettings(difficulty)

    def setDifficultySettings(self, difficulty):
        if difficulty == 1:
            self.speed = 400
            self.food = Food(1, 1)
        elif difficulty == 2:
            self.speed = 300
            self.food = Food(2, 2)
        elif difficulty == 3:
            self.speed = 300
            self.generateWalls()
            self.food = Food(3, 3, self.walls)
        self.text = pygame.font.SysFont('Arial', 16).render('HRH', True, (200, 44, 44))

    def display(self):
        self.screen.fill(gameColors['background'])
        self.scoreboard.display(self.screen, gameColors['scoreboard'])
        self.gameboard.display(self.screen, gameColors['gameboard'])
        for wall in self.walls:
            wall.display(self.screen)
        self.snake.display(self.screen)
        self.food.updateFood(self.snake.getTail())
        self.food.display(self.screen)
        if self.pause:
            self.pausePage.display(self.screen)
        pygame.display.update()

    def generateWalls(self):
        for i in range(0, 5):
            wall = Wall()
            self.walls.append(wall)

    def snakeEatsFood(self):
        snake = self.snake.getHead()
        foods = self.food.getFoodList()
        for food in foods:
            if food.isCollide(snake):
                self.food.removeFood(food)
                self.snake.addBody()
                self.scoreboard.addScore(self.difficulty, food.returnTypeFood())

    def eventsHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.pause = True
                self.pausePage = Pause(self.screen, self.pause)
            self.snake.setDirection()        

    def checkIfCollide(self):
        coords = self.snake.getHead().getCoords()
        head = self.snake.getHead()
        tail = self.snake.getTail()
        if coords[0] < 0:
            self.action = 'result'
            self.running = False
        if coords[0] > 12:
            self.action = 'result'
            self.running = False
        if coords[1] < 0:
            self.action = 'result'
            self.running = False
        if coords[1] > 12:
            self.action = 'result'
            self.running = False
        for ta in tail:
            if ta.isCollide(head):
                self.action = 'result'
                self.running = False
        for wall in self.walls:
            if wall.collide(head):
                self.action = 'result'
                self.running = False

    def getResults(self):
        return (self.nickname, self.scoreboard.score, self.difficulty, self.scoreboard.getTimeInSeconds())

    def moveSnake(self, dt):
        self.lastActionTime += dt
        if self.lastActionTime > self.speed:
            self.snake.move()
            self.lastActionTime = 0

    def changeTime(self, time):
        self.timeElapsed += time.tick()
        if self.timeElapsed > self.second:
            self.scoreboard.addSecond()
            self.timeElapsed = 0
    
    def addExtraScoreForTime(self, time):
        self.timeElapsedExtra += time.tick()
        if self.timeElapsedExtra > 20000:
            self.scoreboard.addScoreForTime(100)
            self.timeElapsedExtra = 0

    def addSpeedEvery10Seconds(self, time):
        self.timeElapsedExtra += time.tick()
        if self.timeElapsedExtra > 10000:
            if self.speed != 100:
                self.speed -= 20
            self.timeElapsedExtra = 0

    def getAction(self):
        return self.action

    def start(self):
        clock = pygame.time.Clock()
        time = pygame.time.Clock()
        timeExtraScore = pygame.time.Clock()
        timeExtraSpeed = pygame.time.Clock()
        while self.running:
            if self.pause != True:
                self.eventsHandler()
                self.display()
                self.moveSnake(clock.tick())
                self.snakeEatsFood()
                self.checkIfCollide()
                self.changeTime(time)
                if self.difficulty == 3:
                    self.addExtraScoreForTime(timeExtraScore)
                    self.addSpeedEvery10Seconds(timeExtraSpeed)
            else:
                option = self.pausePage.getOption()
                if option == "resume":
                    self.pause = False
                elif option == "menu":
                    self.running = False
                    self.action = 'menu'
                self.pausePage.eventsHandler()
                self.display()









