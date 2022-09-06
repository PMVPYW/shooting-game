import time
import pygame

from Playable import Playable


class Enemy(Playable):
    def __init__(self,  x, y):
        super().__init__(x, y, -1)
        self.color = (255,0,0)
        self.nextShoot+=5
