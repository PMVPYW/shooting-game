import time
import pygame
from random import uniform as rand
from Bullet import Bullet

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
            self.nextMove = time.time() + 0.05
            self.x+=self.xDeslocation
            self.y+=self.yDeslocation