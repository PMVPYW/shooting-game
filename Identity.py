import time
import pygame
import pyautogui

class Identity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xDeslocation = 5
        self.yDeslocation = 0
        self.health = 100
        self.width = 25
        self.height = 25
        self.color = (255,255,255)
        self.nextMove = time.time()+0.05



    def draw(self, screen: pygame.display):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


    def move(self):
        if time.time() >= self.nextMove:
            maxX, maxY = pyautogui.size()
            self.nextMove = time.time() + 0.05
            if self.x+self.xDeslocation >= maxX or self.x+self.xDeslocation <= 0:
                self.xDeslocation*=-1

            self.x+=self.xDeslocation
            if self.y+self.yDeslocation >= maxY or self.y+self.yDeslocation <= 0:
                self.yDeslocation*=-1
            self.y+=self.yDeslocation