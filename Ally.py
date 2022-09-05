import time
import pygame
from Identity import Identity
from Playable import Playable
import random


class Ally(Playable):
    def __init__(self,  x, y):
        super(x, y)
        self.color = (0,255,0)

    def watchEnvironment(self, allies: Playable, enemys: Playable, bullets: Identity):
        for alli in allies:
            if alli.x >= self.x-self.width and alli.x <= self.x+self.width:
                self.nextShoot+=0.05
                self.xDeslocation = random.randint(-1, 1)
                if alli.y >= self.y and alli.y <= self.x+self.height:
                    self.yDeslocation = random.randint(-1, 1)
