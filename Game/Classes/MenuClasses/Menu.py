import pygame, os, sys
from Game.Utils.Screen import Screen
from Game.Classes.GameClasses import Game
from Game.Classes.MenuClasses.Nickname import Nickname
from Game.Classes.MenuClasses.Difficulty import Difficulty
from Game.Classes.MenuClasses.About import About
from Game.Utils.Colors import menuColors

pattayaFont = os.getcwd() + "/Game/assets/Pattaya-Regular.ttf"
arimoFont = os.getcwd() + "/Game/assets/Arimo.ttf"
snakeImage = os.getcwd() + "/Game/assets/snake.png"

class Menu(Screen):
    
    def __init__(self):
        super().__init__()

        self.action = ''
        
        self.page = 'menu'
        self.nickname = "anonymous"
        self.option = 1
        self.difficulty_option = 1
        self.running = True
        
        self.pageNameFont = pygame.font.Font(pattayaFont, 50)
        self.optionFont = pygame.font.Font(arimoFont, 35)
        self.informationFont = pygame.font.Font(arimoFont, 15)
        
        self.snakeImage = pygame.image.load(snakeImage)

        self.rectSelectedOption = pygame.Rect(10, 144, 510, 55)
        
        self.pageName = self.pageNameFont.render("Snake", True, menuColors['pageName'])
        self.userLabel = self.informationFont.render("User: anonymous", True, menuColors['label'])
        self.difficultyLabel = self.informationFont.render("Difficulty: easy", True, menuColors['label'])
        
        self.confirmLabel = self.informationFont.render("Confirm -> Enter", True, menuColors['navigation'])
        
        self.startOption = self.optionFont.render("Start", True, menuColors['option_selected'])
        self.nicknameOption = self.optionFont.render("Nickname", True, menuColors['option'])
        self.difficultyOption = self.optionFont.render("Difficulty", True, menuColors['option'])
        self.aboutOption = self.optionFont.render("About", True, menuColors['option'])
        self.exitOption = self.optionFont.render("Exit", True, menuColors['option'])

    def display(self):
        self.changeDifficultyLabel()
        self.changeUserLabel()
        self.screen.fill(menuColors['background'])
        self.screen.blit(self.snakeImage, (30, 10))
        self.screen.blit(self.pageName, ((self.width-self.pageName.get_width())/2, 10))
        self.screen.blit(self.userLabel, ((self.width-self.userLabel.get_width())/2, 85))
        self.screen.blit(self.confirmLabel, (380, 25))
        self.screen.blit(self.difficultyLabel, ((self.width-self.difficultyLabel.get_width())/2, 105))
        self.gradientRect(self.screen, menuColors['background'], menuColors['gradient_01'], menuColors['gradient_02'], menuColors['gradient_01'], menuColors['background'], self.rectSelectedOption)
        self.screen.blit(self.startOption, ((self.width-self.startOption.get_width())/2, 150))
        self.screen.blit(self.nicknameOption, ((self.width-self.nicknameOption.get_width())/2, 230))
        self.screen.blit(self.difficultyOption, ((self.width-self.difficultyOption.get_width())/2, 310))
        self.screen.blit(self.aboutOption, ((self.width-self.aboutOption.get_width())/2, 390)) 
        self.screen.blit(self.exitOption, ((self.width-self.exitOption.get_width())/2, 470))
        pygame.display.update()

    def changeDifficultyLabel(self):
        if self.difficulty_option == 1:
            self.difficultyLabel = self.informationFont.render("Difficulty: easy", True, menuColors['label'])
        if self.difficulty_option == 2:
            self.difficultyLabel = self.informationFont.render("Difficulty: medium", True, menuColors['label'])
        if self.difficulty_option == 3:
            self.difficultyLabel = self.informationFont.render("Difficulty: hard", True, menuColors['label'])

    def changeUserLabel(self):
        nickname = "User: " + self.nickname
        self.userLabel = self.informationFont.render(nickname, True, menuColors['label'])

    def gradientRect(self, window, left, middle, middle2, middle3, right, target_rect):
        color_rect = pygame.Surface((5, 2))
        pygame.draw.line(color_rect, left, (0,0),(0,1))
        pygame.draw.line(color_rect, middle, (1,0), (1,1))
        pygame.draw.line(color_rect, middle2, (2,0), (2,1))
        pygame.draw.line(color_rect, middle3, (3,0), (3,1))
        pygame.draw.line(color_rect, right, (4,0), (4,1))
        color_rect = pygame.transform.smoothscale(color_rect, (target_rect.width, target_rect.height))
        window.blit(color_rect, target_rect)  

    def changeOption(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.option != 1:
                self.rectSelectedOption = self.rectSelectedOption.move(0, -80)
                self.option -= 1
        if keys[pygame.K_DOWN]:
            if self.option != 5:
                self.rectSelectedOption = self.rectSelectedOption.move(0, 80)
                self.option += 1
        self.resetRectSelected()
        if self.option == 1:
            self.startOption = self.optionFont.render("Start", True, menuColors['option_selected'])
        if self.option == 2:
            self.nicknameOption = self.optionFont.render("Nickname", True, menuColors['option_selected'])
        if self.option == 3:
            self.difficultyOption = self.optionFont.render("Difficulty", True, menuColors['option_selected'])
        if self.option == 4:
            self.aboutOption = self.optionFont.render("About", True, menuColors['option_selected'])
        if self.option == 5:
            self.exitOption = self.optionFont.render("Exit", True, menuColors['option_selected'])

    def resetRectSelected(self):
        self.startOption = self.optionFont.render("Start", True, menuColors['option'])
        self.nicknameOption = self.optionFont.render("Nickname", True, menuColors['option'])
        self.difficultyOption = self.optionFont.render("Difficulty", True, menuColors['option'])
        self.aboutOption = self.optionFont.render("About", True, menuColors['option'])
        self.exitOption = self.optionFont.render("Exit", True, menuColors['option'])
            
    def selectOption(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if self.option == 1:
                self.action = 'startGame'
                self.running = False
            elif self.option == 2:
                self.nicknamePage = Nickname(self.screen, self.nickname)
                self.page = "nickname"
            elif self.option == 3:
                self.difficultyPage = Difficulty(self.screen, self.difficulty_option)
                self.page = "difficulty"
            elif self.option == 4:
                self.aboutPage = About(self.screen)
                self.page = "about"
            elif self.option == 5:
                self.action = 'exit'
                self.running = False

    def eventsHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            self.changeOption()
            self.selectOption()

    def menuOptionHandler(self):
        self.eventsHandler()
        self.display()

    def aboutOptionHandler(self):
        self.aboutPage.events()
        self.aboutPage.display()
        self.page = self.aboutPage.returnPage()

    def difficultyOptionHandler(self):
        self.difficultyPage.events()
        self.difficultyPage.display()
        option = self.difficultyPage.returnOption()
        if option == "back":
            self.page = "menu"
        elif option == "confirm":
            self.page = "menu"
            self.difficulty_option = self.difficultyPage.returnDifficultyOption()

    def nicknameOptionHandler(self):
        self.nicknamePage.events()
        self.nicknamePage.display()
        option = self.nicknamePage.returnOption()
        if option == "back":
            self.page = "menu"
        elif option == "confirm":
            self.page = "menu"
            self.nickname = self.nicknamePage.returnNickname()
        
    def getSettings(self):
        return (self.screen, self.nickname, self.difficulty_option)

    def returnAction(self):
        return self.action

    def run(self):
        self.running = True
        while self.running:
            if self.page == "menu":
                self.menuOptionHandler()
            if self.page == "nickname":
                self.nicknameOptionHandler()
            if self.page == "difficulty":
                self.difficultyOptionHandler()
            if self.page == "about":
                self.aboutOptionHandler()