import pygame
import time
from threading import Thread
import pyautogui
from Identity import Identity


class Bullet(Identity):
    def __init__(self, x, y, Deslocation: int, id: int):
        super().__init__(x, y)
        self.height = 5
        self.width = 5
        self.color = (255,255,0)
        self.nextMove = time.time()+0.5
        self.exists = True
        self.xDeslocation = 0
        self.yDeslocation = 5*Deslocation
        self.id = id

    def move(self):
        if time.time() >= self.nextMove:
            maxX, maxY = pyautogui.size()
            self.nextMove = time.time() + 0.05
            self.x+=self.xDeslocation
            self.y+=self.yDeslocation

    def runFunction(self, screen):
        if self.exists:
            self.move()
            self.draw(screen)

    def run(self, screen):
        self.runFunction(screen)

    def ReadyToDelete(self):
        if self.exists:
            maxX, maxY = pyautogui.size()
            if self.x > maxX or self.x < 0 or self.y > maxY or self.y < 0:
                self.exists = False
                return True
        return False
