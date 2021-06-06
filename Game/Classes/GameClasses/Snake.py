import pygame
from Game.Classes.GameClasses.SnakePart import SnakePart

class Snake:

    def __init__(self):
        self.tail = []
        self.direction = 'right' #left, right, up, down
        self.lastDirection = 'right'
        self.rect = SnakePart(6, 5, "end" , 'right')
        self.rect1 = SnakePart(6, 6, "part", 'right')
        self.rect2 = SnakePart(6, 7, "head", 'right')
        self.tail.append(self.rect)
        self.tail.append(self.rect1)
        self.tail.append(self.rect2)
        self.eats = False

    def getHead(self):
        return self.tail[-1]

    def getTail(self):
        return self.tail[:-1]

    def addBody(self):
        coords = self.tail[0].getCoords()
        part = SnakePart(coords[0], coords[1], 'part', self.tail[1].getDirection())
        self.tail.insert(0, part)
        self.tail[0].changePart('end')
        self.tail[1].changePart('end')

    def display(self, surface):
        for item in self.tail:
            item.displaySnakePart(surface)

    def setDirection(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.lastDirection != 'right':
                self.direction = 'left'
        if keys[pygame.K_RIGHT]:
            if self.lastDirection != 'left':
                self.direction = 'right'
        if keys[pygame.K_UP]:
            if self.lastDirection != 'down':
                self.direction = 'up'
        if keys[pygame.K_DOWN]:
            if self.lastDirection != 'up':
                self.direction = 'down'

    def setPicturesForBody(self, tail):
        countTail = len(tail)
        for i in range(0, countTail - 1):
            if i >= 1 and i <= countTail:
                _current = tail[i]
                _prev = tail[i-1]
                _next = tail[i+1]
                if _prev.getDirection() == 'right' and _current.getDirection() == "right" and _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("right")
                if _prev.getDirection() == 'left' and _current.getDirection() == "left" and _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("left")
                if _prev.getDirection() == 'down' and _current.getDirection() == "down" and _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("down")
                if _prev.getDirection() == 'up' and _current.getDirection() == "up" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("up")

                if _prev.getDirection() == 'left' and _current.getDirection() == "left" and _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("left-down")
                if _prev.getDirection() == 'right' and _current.getDirection() == "right" and _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("right-down")

                if _prev.getDirection() == 'down' and _current.getDirection() == "down" and _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("down-right")
                if _prev.getDirection() == 'down' and _current.getDirection() == "down" and _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("down-left")

                if _prev.getDirection() == 'right' and _current.getDirection() == "right" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("right-up")
                if _prev.getDirection() == 'left' and _current.getDirection() == "left" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("left-up")

                if _prev.getDirection() == 'up' and _current.getDirection() == "up" and _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("up-right")
                if _prev.getDirection() == 'up' and _current.getDirection() == "up" and _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("up-left")

                if _prev.getDirection() == 'right' and _current.getDirection() == "up" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("up")
                if _prev.getDirection() == 'left' and _current.getDirection() == "up" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("up")
                if _prev.getDirection() == 'right' and _current.getDirection() == "down" and _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("down")
                if _prev.getDirection() == 'left' and _current.getDirection() == "down" and _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("down")

                if _prev.getDirection() == 'up' and _current.getDirection() == "right" and _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("right")
                if _prev.getDirection() == 'up' and _current.getDirection() == "left" and _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("left")
                if _prev.getDirection() == 'down' and _current.getDirection() == "right" and _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("right")
                if _prev.getDirection() == 'down' and _current.getDirection() == "left" and _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("left")

                if _prev.getDirection() == 'up' and _current.getDirection() == "right" and _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("right-down")
                if _prev.getDirection() == 'up' and _current.getDirection() == "left" and _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("left-down")
                if _prev.getDirection() == 'left' and _current.getDirection() == "up" and _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("up-right")
                if _prev.getDirection() == 'right' and _current.getDirection() == "up" and _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("up-left")
                if _prev.getDirection() == 'left' and _current.getDirection() == "down" and _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("down-right")
                if _prev.getDirection() == 'down' and _current.getDirection() == "right" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("right-up")
                if _prev.getDirection() == 'right' and _current.getDirection() == "down" and _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("down-left")
                if _prev.getDirection() == 'down' and _current.getDirection() == "left" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("left-up")
                if _prev.getDirection() == 'up' and _current.getDirection() == "left" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("left-up")
                if _prev.getDirection() == 'left' and _current.getDirection() == "up" and _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("up-left")
                if _prev.getDirection() == 'left' and _current.getDirection() == "right" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("right-up")
                if _prev.getDirection() == 'right' and _current.getDirection() == "up" and _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("up-right")
                if _prev.getDirection() == 'up' and _current.getDirection() == "right" and _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("right-up")
                if _prev.getDirection() == 'down' and _current.getDirection() == "right" and _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("right-down")
                if _prev.getDirection() == 'down' and _current.getDirection() == "left" and _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("left-down")
                if _prev.getDirection() == 'left' and _current.getDirection() == "down" and _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("down-left")
                if _prev.getDirection() == 'right' and _current.getDirection() == "down" and _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("down-right")

            if i == 0:
                _next = _next = tail[i+1]
                if _next.getDirection() == 'right':
                    tail[i].setDirectionPicture("right")
                if _next.getDirection() == 'left':
                    tail[i].setDirectionPicture("left")
                if _next.getDirection() == 'down':
                    tail[i].setDirectionPicture("down")
                if _next.getDirection() == 'up':
                    tail[i].setDirectionPicture("up")

    def move(self):
        countTail = len(self.tail)
        if self.direction == 'left':
            for i in range(0, countTail):
                if i != countTail-1:
                    temp = self.tail[i+1].getCoords()
                    tempDirection = self.tail[i+1].getDirection()
                    self.tail[i].setPosition(temp[0], temp[1])
                    self.tail[i].setDirection(tempDirection)
                else:
                    x = self.tail[i].getCoords()[0]
                    y = self.tail[i].getCoords()[1] - 1
                    self.tail[i].setPosition(x, y)
                    self.tail[i].setDirection('left')
                    self.tail[i].setDirectionPicture('left')
            self.lastDirection = 'left'
        if self.direction == 'right':
            for i in range(0, countTail):
                if i != countTail-1:
                    temp = self.tail[i+1].getCoords()
                    tempDirection = self.tail[i+1].getDirection()
                    self.tail[i].setPosition(temp[0], temp[1])
                    self.tail[i].setDirection(tempDirection)
                else:
                    x = self.tail[i].getCoords()[0]
                    y = self.tail[i].getCoords()[1] + 1
                    self.tail[i].setPosition(x, y)
                    self.tail[i].setDirection('right')
                    self.tail[i].setDirectionPicture('right')
            self.lastDirection = 'right'
        if self.direction == 'up':
            for i in range(0, countTail):
                if i != countTail-1:
                    temp = self.tail[i+1].getCoords()
                    tempDirection = self.tail[i+1].getDirection()
                    self.tail[i].setPosition(temp[0], temp[1])
                    self.tail[i].setDirection(tempDirection)
                else:
                    x = self.tail[i].getCoords()[0] - 1
                    y = self.tail[i].getCoords()[1]
                    self.tail[i].setPosition(x, y)
                    self.tail[i].setDirection('up')
                    self.tail[i].setDirectionPicture('up')
            self.lastDirection = 'up'
        if self.direction == 'down':
            for i in range(0, countTail):
                if i != countTail-1:
                    temp = self.tail[i+1].getCoords()
                    tempDirection = self.tail[i+1].getDirection()
                    self.tail[i].setPosition(temp[0], temp[1])
                    self.tail[i].setDirection(tempDirection)
                else:
                    x = self.tail[i].getCoords()[0] + 1
                    y = self.tail[i].getCoords()[1]
                    self.tail[i].setPosition(x, y)
                    self.tail[i].setDirection('down')
                    self.tail[i].setDirectionPicture('down')
            self.lastDirection = 'down'
        self.setPicturesForBody(self.tail)
        for i in range(0, len(self.tail)-1):
            if i == 0:
                self.tail[i].changePart('end')
            else:
                self.tail[i].changePart('part')

