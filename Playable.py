import time
import pygame
import pyautogui
from random import uniform as rand
from Bullet import Bullet
from Identity import Identity


class Playable(Identity):
    def __init__(self, x, y, ammoDir: int):
        super().__init__(x, y)
        self.nextShoot = time.time() + 0.5
        self.ammoDirection = ammoDir
        self.lastId = 0

    def shoot(self):
        if time.time() < self.nextShoot:
            return
        self.nextShoot = time.time()+rand(1, 2.5)
        return Bullet(self.x+self.width/2,self.y, self.ammoDirection, 0)


    def runFunction(self, screen, enemys):
        if self.health > 0:
            self.draw(screen)
            if len(enemys) != 0:
                self.move()
                return self.shoot()

    def run(self, screen, enemys):
        return self.runFunction(screen, enemys)

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
            if self.y < 0:
                self.y = 0
            elif self.y > maxY-self.height:
                self.y = maxY-self.height

