import time
import pygame
from Identity import Identity
from Playable import Playable
import random


class Ally(Playable):
    def __init__(self,  x: int, y: int):
        super().__init__(x, y)
        self.color = (0,255,0)

    def watchEnvironment(self, allies: Playable, enemys: Playable, bullets: Identity, maxX: int, maxY: int):
        if self.x <= 0:
            self.xDeslocation = 1
            return
        elif self.x >= maxX:
            self.xDeslocation = -1
            return
        if self.y <= 0:
            self.yDeslocation = 1
            return
        elif self.x >= maxY:
            self.yDeslocation = -1
            return

        for alli in allies:
            if alli.x >= self.x-self.width and alli.x <= self.x+self.width:
                self.nextShoot= time.time() + 0.05
                self.xDeslocation = random.randint(-1, 1)
                if alli.y >= self.y and alli.y <= self.x+self.height:
                    self.yDeslocation = random.randint(-1, 1)
                return

        for bullet in bullets:
            break

