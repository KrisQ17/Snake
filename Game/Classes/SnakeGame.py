from Game.Classes.GameClasses.Result import Result
from time import time
import pygame
from Game.Classes.MenuClasses.Menu import Menu
from Game.Classes.GameClasses.Game import Game


class SnakeGame:

    def __init__(self):
        pygame.init()

    def start(self):
        menu = Menu()
        action = ""
        while action != "exit":
            menu.run()
            action = menu.returnAction()
            if action == 'exit':
                break
            elif action == 'startGame':
                settings = menu.getSettings()
                screen = settings[0]
                nickname = settings[1]
                difficulty = settings[2]
                game = Game(screen, nickname, difficulty)
                game.start()
                gameAction = game.getAction()
                if gameAction == "result":
                    results = game.getResults()
                    resultPage = Result(results)
                    resultPage.run()
                    resultAction = resultPage.returnAction()
                    if resultAction == 'exit':
                        break
        pygame.quit()



