import pygame, random
from Game.Classes.GameClasses.FoodPart import FoodPart

class Food():

    def __init__(self, amount, types, walls=None):
        self.foodList = []
        self.max_row = 12 # 0-12
        self.max_column = 12 # 0-12
        self.amountFoodOnBoard = 0
        self.amount = amount
        self.types = types
        self.walls = walls

    def makeFood(self, tail):
        isCollide = False
        row = random.randint(0, self.max_row)
        column = random.randint(0, self.max_column)
        typeFood = random.randint(1, self.types)
        food = FoodPart(row, column, typeFood)
        for item in tail:
            if item.isCollide(food):
                print(food.getCoords())
                print(item.getCoords())
                isCollide = True
        if self.walls != None:
            for wall in self.walls:
                if wall.collide(food):
                    isCollide = True
        if isCollide == False:
            self.foodList.append(food)
            self.amountFoodOnBoard += 1
            return True
        else:
            return False

    def updateFood(self, tail):
        if self.amountFoodOnBoard < self.amount:
            newfood = self.makeFood(tail)
            while newfood != True:
                newfood = self.makeFood(tail)

    def getFoodList(self):
        return self.foodList;

    def display(self, surface):
        for item in self.foodList:
            item.display(surface)

    def removeFood(self, food):
        self.foodList.remove(food)
        self.amountFoodOnBoard -= 1

        